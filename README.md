# ArXivPully
An API that can return articles from the ArXiv database for development purposes. Using Falcon to build a local API and ngrok to expose the local web server. Running the Python script ArXivPully.py to build it all.

Requires Falcon API and ngrok

# How to Use ArXivPully
Call using url: http://31d2d04a.ngrok.io/api/query and query by adding "?<term_1>=<number_of_articles>&<term_2>=<number_of_articles>..."
Separate queries by &


Example: I want 10 articles about "clustering" from ArXiv, call http://31d2d04a.ngrok.io/api/query?clustering=10 

The result will be in the form of ["pdf link","Paper Title","Paper Body"] for each article sent in

# Known Issues
Using space delimited phrases like "data mining" will not interpret results properly

Math Formatting will look like a mess in certain articles
