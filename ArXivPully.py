from falcon import API
from urllib import request
from bs4 import BeautifulSoup

class ArXivPully:
    # Removes rogue newline characters from the title and abstract
    def cleanText(self,text):
        return ' '.join(text.split('\n'))

    def pullFromArXiv(self,search_query, num_results=10):
        url = 'https://export.arxiv.org/api/query?search_query=all:'+search_query+'&start=0&max_results='+str(num_results)
        data = request.urlopen(url).read()
        output = []
        soup = BeautifulSoup(data, 'html.parser')
        titles = soup.find_all('title')

        # ArXiv populates the first title value as the search query
        titles.pop(0)

        bodies = soup.find_all('summary')
        links = soup.find_all('link', title='pdf')
        for i in range(len(titles)):
            title = self.cleanText(titles[i].text.strip())
            body = self.cleanText(bodies[i].text.strip())
            pdf_link = links[i]['href']
            output.append([pdf_link, title, body])
        return output

    def on_get(self, req, resp):
        """Handles GET requests"""
        output = []
        for item in req.params.items():
            output.append(self.pullFromArXiv(item[0],item[1]))
        resp.media = output

api = API()
api.add_route('/api/query', ArXivPully())
