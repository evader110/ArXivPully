import falcon
from urllib import request
from bs4 import BeautifulSoup

class ArXivPully:
    def pullFromArxiv(self,search_query, num_results=10):
        url = 'https://export.arxiv.org/api/query?search_query=all:'+search_query+'&start=0&max_results='+str(num_results)
        data = request.urlopen(url).read()
        output = []
        soup = BeautifulSoup(data, 'html.parser')
        titles = soup.find_all('title')
        titles.pop(0)
        bodies = soup.find_all('summary')
        links = soup.find_all('link', title='pdf')
        for i in range(len(titles)):
            title = titles[i].text.strip()
            body = bodies[i].text.strip()
            pdf_link = links[i]['href']
            output.append([pdf_link, title, body])
        return output

    def on_get(self, req, resp):
        """Handles GET requests"""
        output = []
        for item in req.params.items():
            output.append(self.pullFromArxiv(item[0],item[1]))
        resp.media = output

api = falcon.API()
api.add_route('/api/', ArXivPully())
