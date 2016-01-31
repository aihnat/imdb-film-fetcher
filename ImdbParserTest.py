import unittest
import ImdbParser
from bs4 import BeautifulSoup

class ImdbParserTest(unittest.TestCase):

    def test_valid_filter_films_tag(self):
        self.assertTrue(
            ImdbParser.filter_films_tag(
                BeautifulSoup('<td class="titleColumn"><span name="ir" data-value="9,21">1.</span>'
                              '<a href="/title/tt0111161/?ref_=chttp_tt_1" title="Frank Darabont (dir.), Tim Robbins, Morgan Freeman">Skazani na Shawshank</a>'
                              '<span name="rd" data-value="1994-10-14" class="secondaryInfo">(1994)</span></td>', 'lxml').td))

    def test_invalid_filter_films_tag(self):
        self.assertFalse(ImdbParser.filter_films_tag(
            BeautifulSoup('<td class="posterColumn"><a href="/title/tt0111161/?ref_=chttp_tt_1">'
                          '<img src="http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX34_CR0,0,34,50_AL_.jpg" width="34" height="50">'
                          '</a></td>', 'lxml')
        ))

    def test_valid_get_film(self):
        self.assertEquals('tt0111161', ImdbParser.get_film_id(BeautifulSoup('<td class="posterColumn"><a href="/title/tt0111161/?ref_=chttp_tt_1">'
                          '<img src="http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX34_CR0,0,34,50_AL_.jpg" width="34" height="50">'
                          '</a></td>', 'lxml')))

    def test_get_films(self):
        self.assertEquals(['tt0111161', 'tt0111161'],
                          ImdbParser.get_film_ids('<td class="titleColumn"><a href="/title/tt0111161/?ref_=chttp_tt_1">'
                          '<img src="http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX34_CR0,0,34,50_AL_.jpg" width="34" height="50">'
                          '</a></td>'
                          '<td class="titleColumn"><a href="/title/tt0111161/?ref_=chttp_tt_1">'
                          '<img src="http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX34_CR0,0,34,50_AL_.jpg" width="34" height="50">'
                          '</a></td>'))

    def test_get_no_films(self):
        self.assertEquals([],
                          ImdbParser.get_film_ids('<td class="posterColumn"><a href="/title/tt0111161/?ref_=chttp_tt_1">'
                          '<img src="http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX34_CR0,0,34,50_AL_.jpg" width="34" height="50">'
                          '</a></td>'
                          '<td class="posterColumn"><a href="/title/tt0111161/?ref_=chttp_tt_1">'
                          '<img src="http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX34_CR0,0,34,50_AL_.jpg" width="34" height="50">'
                          '</a></td>'))
