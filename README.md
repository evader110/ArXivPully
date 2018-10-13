# ArXivPully
An API that can return articles from the ArXiv database for development purposes

# How to Use ArXivPully
Call using url: http://localhost:8000/api/ and query by adding "?<term_1>=<number_of_articles>&<term_2>=<number_of_articles>..."
Separate queries by &


Example: I want 10 articles about "clustering" from ArXiv, call http://localhost:8000/api/?clustering=10 
