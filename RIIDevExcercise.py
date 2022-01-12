
import requests
import json
from datetime import date

def main():

	api_root = "https://p8doqtvi9f.execute-api.us-west-2.amazonaws.com/rii-dev-interview"
	api_url_books = f"{api_root}/books"
	api_url_authors = f"{api_root}/authors"

	books_response = requests.get(api_url_books)
	authors_response = requests.get(api_url_authors)
	books = books_response.json()
	authors = authors_response.json()

	impossible_books = []
	for book in books:
		author_name = book["author"]

		for author in authors:
			if author["name"] == author_name:
				if (check_author_validity(book, author) is False):
					impossible_books.append(book)

	print_result(impossible_books)





def check_author_validity(book, author):
	illegal_books = []

	publication_date = book["published"]
	publication_year = publication_date.split("-")[2]  # Date format is dd-mm-yy

	author_age = author["age"]
	current_year = date.today().year
	age_at_publication = author_age - (current_year - int(publication_year))
	# print(f"{book['title']} - {publication_date} | {author['name']} {author['age']}")
	# print(age_at_publication)

	if (age_at_publication < 10):
		return False
	elif (age_at_publication == 10):
		return True
		# Edge case.
		# The specification guarantees the author's birthday

	return True

def print_result(books):
	print("The following books could not have been written by their author listed in the database:")

	i = 1
	for book in books:
		print(f"{i}) {book['title']}")
		print(f"Author: {book['author']}")
		print(f"Age at publication: ")
		print()
		i += 1

main()
