# ArXivPully
An API that can return articles from the ArXiv database for development purposes

# How to Use ArXivPully
Call using url: http://localhost:8000/api/ and query by adding "?<term_1>=<number_of_articles>&<term_2>=<number_of_articles>..."
Separate queries by &


Example: I want 10 articles about "clustering" from ArXiv, call http://localhost:8000/api/?clustering=10 

The result will be in the form of ["pdf link","Paper Title","Paper Body"] for each article sent in

# Known Issues
Using space delimited phrases like "data mining" will not interpret results properly
Math Formatting will look like a mess in certain articles
