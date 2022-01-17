"""RII Dev Excercise

This script references data stored in AWS containing a list of books and authors

Books have the following fields:
type: str = "book"
title: str
author: str (corresponds to "name" field of an author object)
published: str (formatted "day-month-year" where day, month, and year are integers)

Authors have the following fields:
type: str = "author"
name: str
age: int

This script performs the following:
1) Pulls the book and author data using HTTP Get requests
2) Matches each book to its corresponding author
3) Calculates the author's age at the book's listed year of publication
4) Prints out the books whose author's are too young (age < 10 at publication)

This script requires that `requests` be installed within the Python
environment you are running this script in. ("pip install requests")
"""

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

	impossible_books = check_books(books, authors)
	print_result(impossible_books)


def check_books(books: list, authors: list) -> list:
	"""Takes a list of books and authors and returns a list of books
		whose authors are too young (< 10 years old when published)"""

	impossible_books = []
	for book in books:
		author_name = book["author"]

		for author in authors:
			if author["name"] == author_name:
				if (check_author_validity(book, author) is False):
					impossible_books.append(book)
				break  # We found the author, no need to continue looping

	return impossible_books


def check_author_validity(book: dict, author: dict) -> bool:
	"""For a given book and author:
	Returns false if the author's age is less than 10 when the book was published
	Returns true otherwise
	"""

	publication_date = book["published"]
	publication_year = publication_date.split("-")[2]  # Date format is dd-mm-yyyy

	author_age = author["age"]
	current_year = date.today().year
	age_at_publication = author_age - (current_year - int(publication_year))

	if (age_at_publication < 10):
		return False
	elif (age_at_publication == 10):
		return True
		# Edge case.
		# Normally we would need check the author's birthday against the publication date.
		# However the specification guarantees the edge case does not exist in this data set.

	return True


def print_result(books: list):
	"""Prints out the given list of books"""

	print("The following books could not have been written by their author listed in the data set:")

	i = 1
	for book in books:
		print(f"{i}) {book['title']}")
		print(f"Listed author: {book['author']}")
		print()
		i += 1


main()
