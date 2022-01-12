
import requests
import json

api_root = "https://p8doqtvi9f.execute-api.us-west-2.amazonaws.com/rii-dev-interview"
api_url_books = f"{api_root}/books"
api_url_authors = f"{api_root}/authors"

books_response = requests.get(api_url_books)
print(books_response.status_code)
print(books_response.json())

authors_response = requests.get(api_url_authors)
print(authors_response.status_code)
print(authors_response.json())


books = books_response.json()
authors = authors_response.json()
for book in books:
	author_name = book["author"]
	publication_date = book["published"]
	year = publication_date.split("-")[2]  # Date format is dd-mm-yy
	for author in authors:
		if author["name"] == author_name:
			print(f"{book['title']} - {year} | {author_name} {author['age']}")
