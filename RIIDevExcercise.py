
import requests

api_root = "https://p8doqtvi9f.execute-api.us-west-2.amazonaws.com/rii-dev-interview"
api_url_books = f'{api_root}/books'
api_url_authors = f'{api_root}/authors'

books_response = requests.get(api_url_books)
print(books_response.status_code)
print(books_response.json())

authors_response = requests.get(api_url_authors)
print(authors_response.status_code)
print(authors_response.json())