import json
import requests
import sys
#################
### VARIABLES ###
#################

tokens = json.load(open("./tokens.json"))
minio_server_url = "http://minio1:9000"
token_name = sys.argv[1]
metrics_path = sys.argv[2]
count_only = True

#################
### FUNCTIONS ###
#################

def report(token_name, metrics_path):
    url = f"{minio_server_url}{metrics_path}"
    token = [t['bearerToken'] for t in tokens if t['jobName'] == token_name][0]
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Decode response, split lines, and filter out comments
        filtered_lines = [
            line for line in response.text.splitlines()
            if not line.startswith("#")
        ]
        metrics_count = len(filtered_lines)
        block_text = "\n".join(filtered_lines)
        return [metrics_count, block_text]
    else:
        print(f"Failed to retrieve metrics for {token_name}. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return [None, None]


def main():
    # Gather metrics for cluster metricsPath
    metrics_count,metrics = report(token_name, metrics_path)
    if metrics_count and metrics is not None:
        if count_only:
            print(f"{token_name} metrics count: {metrics_count}")
            return
        print(f"{token_name} metrics ({metrics_count} Metrics Found): \n{metrics}")
    else:
        print("Failed to retrieve cluster metrics.")
    return None

############
### MAIN ###
############

if __name__ == "__main__":
    main()
