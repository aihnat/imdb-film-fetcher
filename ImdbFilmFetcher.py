from bs4 import BeautifulSoup
import json
import urllib2
import io
import argparse
import sys

import ImdbParser
from OmdbApiClient import RemoteOmdbApiClient

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Fetch top N film title and year info from imdb top 250 films')
    parser.add_argument('-n', type=int, nargs='?', default=10)
    parser.add_argument('--csv', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

    args = parser.parse_args()

    films = ImdbParser.get_film_ids(urllib2.urlopen('http://www.imdb.com/chart/top?ref_=nv_ch_250_4').read())[:int(args.n)]

    omdbApi = RemoteOmdbApiClient('http://www.omdbapi.com/?i=')

    with args.csv as f:
       for film_id in films:
           title, year = omdbApi.get_data(film_id)
           f.write('\'' + title + '\',' + year + '\n')
