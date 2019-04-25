# ArXivPully
An API that can return articles from the ArXiv database for development purposes. Using Falcon to build a local API and is hosted though a virtual machine from Google Cloud Platform. Running the Python script ArXivPully.py to build it all. Uses gunicorn.

# How to Use ArXivPully
Call using url: http://api.arxivpully.us/api/query and query by adding "?<term_1>=<number_of_articles>&<term_2>=<number_of_articles>..."
Separate search queries by &


Example: I want 10 articles about "clustering" from ArXiv, call http://api.arxivpully.us/api/query?clustering=10 

The result will be in JSON dump. 
```
{
  search_term : [
    {
      link : 'articlelink.pdf',
      title : 'articletitle',
      body : 'articlebody'
    },
    ...
  ],
  ...
}
```
