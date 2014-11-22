from bs4 import BeautifulSoup
import urllib2
import re

''' get list of films from imdb top 250 films html'''
def get_film_ids(html):
        soup = BeautifulSoup(html)

        res = []
        for elem in filter(filter_films_tag, soup.find_all('td')):
                res.append(get_film_id(elem))
        return res

def filter_films_tag(tag):
        if 'class' in tag.attrs:
                return tag.attrs['class'] == ['titleColumn']
        return False

def get_film_id(tag):
        return tag.a.attrs['href'].split('/')[2]