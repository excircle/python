#!/usr/bin/env python

import json
import logging
import urllib
from uuid import uuid4

import boto3
import requests
from botocore.client import Config
from flask import Flask, request

boto3.set_stream_logger('boto3.resources', logging.DEBUG)

authorize_url = "https://trial-99999999.okta.com/oauth2/v1/authorize"
token_url = "https://trial-99999999.okta.com/oauth2/v1/token"

callback_uri = "http://localhost:8000/oauth2/callback"

client_id = '0oahf59ud3CUAiFdP698'
client_secret = 'supersecretkey-yi0ZDr0MVjNAik5TfkffqHLPKauxxrkF'

sts_client = boto3.client(
    'sts',
    region_name='us-west-2',
    use_ssl=False,
    endpoint_url='http://minio-load-balancer-123456789.us-west-2.elb.amazonaws.com:9000',
)

app = Flask(__name__)

@app.route('/')
def homepage():
    text = '<a href="%s">Authenticate with Okta</a>'
    return text % make_authorization_url()

def make_authorization_url():
    state = str(uuid4())
    params = {"client_id": client_id,
              "response_type": "code",
              "state": state,
              "redirect_uri": callback_uri,
              "scope": "openid"}
    url = authorize_url + "?" + urllib.parse.urlencode(params)
    return url

@app.route('/oauth2/callback')
def callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error

    authorization_code = request.args.get('code')

    data = {'grant_type': 'authorization_code',
            'code': authorization_code, 'redirect_uri': callback_uri}
    id_token_response = requests.post(
        token_url, data=data, verify=False,
        allow_redirects=False, auth=(client_id, client_secret))

    print('body: ' + id_token_response.text)

    tokens = json.loads(id_token_response.text)
    id_token = tokens.get('id_token')
    
    if not id_token:
        return "Error: id_token not found in response"
    
    print("ID Token: ", id_token)

    response = sts_client.assume_role_with_web_identity(
        RoleArn='arn:minio:iam:::role/dIUx-BmnIqYevLY6moHYLkD25yg', 
        RoleSessionName='test', 
        WebIdentityToken=id_token,
        DurationSeconds=3600
    )
    
    credentials = response.get('Credentials')
    
    if not credentials:
        return "Error: Unable to assume role with web identity"
    
    print("Credentials: ", credentials)

    s3_resource = boto3.resource('s3',
                                 endpoint_url='http://minio-load-balancer-123456789.us-west-2.elb.amazonaws.com:9000',
                                 aws_access_key_id=credentials['AccessKeyId'],
                                 aws_secret_access_key=credentials['SecretAccessKey'],
                                 aws_session_token=credentials['SessionToken'],
                                 config=Config(signature_version='s3v4'),
                                 region_name='us-west-2')

    bucket = s3_resource.Bucket('python-test-bucket')

    for obj in bucket.objects.all():
        print(obj)

    return "success"

if __name__ == '__main__':
    app.run(debug=True, port=8000)

