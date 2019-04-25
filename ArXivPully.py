from falcon import API
import requests
from bs4 import BeautifulSoup
import json

class ArXivPully:
    def pull_from_arxiv(self,search_query, num_results=10):
        url = 'https://export.arxiv.org/api/query'
        params = {'search_query': f'all:{search_query}',
                  'start': 0,
                  'max_results': num_results} 
        data = requests.get(url,params=params).text
        soup = BeautifulSoup(data, 'lxml')
        # ArXiv populates the the first title value as the search query 
        titles = soup.find_all('title')[1:]
        bodies = soup.find_all('summary')
        links = soup.find_all('link', title='pdf')
        for title, body, link in zip(titles, bodies, links):
            yield {'link': link['href'],
                'title': title.text.strip().replace('\n',' '),
                'body': title.text.strip().replace('\n',' ')}
               

    def on_get(self, req, resp):
        """Handles GET requests"""
        # json.dumps([list(self.pull_from_arxiv(search_query,num_results) for search_query, num_results in req.params.items())])
        resp.media = json.dumps({search_query : list(self.pull_from_arxiv(search_query, num_results)) for search_query, num_results in req.params.items()})

api = API()
api.add_route('/api/query', ArXivPully())