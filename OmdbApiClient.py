import urllib2
import json

class OmdbApiClient:

    def get_data(self, id):
        pass

class MockOmdbApiClient(OmdbApiClient):

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def get_data(self, id):
        return (self.title, self.year)

class RemoteOmdbApiClient(OmdbApiClient):

    def __init__(self, url):
        self.url = url

    def get_data(self, id):
        json_data = json.loads(urllib2.urlopen(self.url + id).read())
        return (json_data['Title'], json_data['Year'])