import json
import unittest
import requests

class JsonGetMethods(unittest.TestCase):
    def setUp(self):
        self.search_term_one = 'clustering'
        self.search_term_two = 'artificial intelligence'
        self.num_articles_one = 10
        self.num_articles_two = 5
        url = f'http://localhost:8000/api/query?{self.search_term_one}={self.num_articles_one}&{self.search_term_two}={self.num_articles_two}'
        self.data = json.loads(requests.get(url).json())

    def test_json_loads(self):
        self.assertTrue(self.search_term_one in self.data, f'No {self.search_term_one} articles given')
        self.assertTrue(self.search_term_two in self.data, f'No {self.search_term_two} articles given')
        

    def test_article_body_is_full(self):
        self.assertTrue('title' in self.data[self.search_term_one][0], 'No titles were given')
        self.assertTrue('body' in self.data[self.search_term_one][0], 'No bodies were given')
        self.assertTrue('link' in self.data[self.search_term_one][0], 'No links were given')
        self.assertTrue('title' in self.data[self.search_term_two][0], 'No titles were given')
        self.assertTrue('body' in self.data[self.search_term_two][0], 'No bodies were given')
        self.assertTrue('link' in self.data[self.search_term_two][0], 'No links were given')

    def test_correct_number_of_articles(self):
        self.assertTrue(len(self.data[self.search_term_one]) == self.num_articles_one, f'We did not get {self.num_articles_one} articles, instead we got {len(self.data[self.search_term_one])}')
        self.assertTrue(len(self.data[self.search_term_two]) == self.num_articles_two, f'We did not get {self.num_articles_two} articles, instead we got {len(self.data[self.search_term_two])}')

if __name__=='__main__':
    unittest.main()