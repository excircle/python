import requests
import pandas as pd
import json

class AlbumEntry:
    def __init__(self, artist=None, album=None, release_date=None):
        self.artist = artist
        self.album = album
        self.release_date = release_date

    def __str__(self):
        return f'{self.artist}, {self.album}, {self.release_date}\n'

    def to_dict(self):
        return {
            'artist': self.artist,
            'album': self.album,
            'release date': self.release_date
        }

    def to_json(self):
        return json.dumps(self.to_dict())

def return_wiki_dataframe(url):
    res = requests.get(url)
    tables = pd.read_html(res.text)
    df = tables[1]
    return df[['Title', 'Album details']]

def main():
    url = 'https://en.wikipedia.org/wiki/Tom_Petty_discography'
    data = return_wiki_dataframe(url)
    

    for i in range(len(data)):
        print(data.iloc[i]['Title'])
        print(data.iloc[i]['Album details'])
        print('')

if __name__ == '__main__':
    main()