import requests
from faker import Faker
import random

API_BASE_URL = "http://localhost:8080/api/books"  # Replace with your API base URL

# Function to create a new book using the API
def create_book(title, author):
    data = {"title": title, "author": author}
    response = requests.post(API_BASE_URL, json=data)
    return response

# Function to get a book by its ID using the API
def get_book(book_id):
    url = f"{API_BASE_URL}/{book_id}"
    response = requests.get(url)
    return response

# Function to update a book by its ID using the API
def update_book(book_id, title, author):
    url = f"{API_BASE_URL}/{book_id}"
    data = {"title": title, "author": author}
    response = requests.put(url, json=data)
    return response

# Function to delete a book by its ID using the API
def delete_book(book_id):
    url = f"{API_BASE_URL}/{book_id}"
    response = requests.delete(url)
    return response

# Function to print green message
def print_green(msg):
    print("\033[92m{}\033[00m".format(msg))

# Function to print red message
def print_red(msg):
    print("\033[91m{}\033[00m".format(msg))

if __name__ == "__main__":
    # Initialize Faker library
    fake = Faker()

    # Number of fake books to create
    num_books = 10

    created_book_ids = []  # To store the IDs of the books created

    for _ in range(num_books):
        # Generate fake book title and author
        title = fake.catch_phrase()
        author = fake.name()

        # Create a book and get its ID
        response = create_book(title, author)
        if response.status_code == 200:
            book = response.json()
            created_book_ids.append(book['id'])  # Store the book ID
            print_green(f"Book created: {title} by {author}")
        else:
            print_red(f"Failed to create book: {title} by {author}")

    # Test GET method for a random book
    random_book_id = random.choice(created_book_ids)
    response = get_book(random_book_id)
    if response.status_code == 200:
        book = response.json()
        print_green(f"Book ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
    else:
        print_red(f"Failed to get book with ID: {random_book_id}")

    # Test PUT method for a random book
    random_book_id = random.choice(created_book_ids)
    response = update_book(random_book_id, "Updated Book Title", "Updated Author Name")
    if response.status_code == 200:
        print_green(f"Book updated with ID: {random_book_id}, Title: Updated Book Title, Author: Updated Author Name")
    else:
        print_red(f"Failed to update book with ID: {random_book_id}")

    # Test DELETE method for a random book
    random_book_id = random.choice(created_book_ids)
    response = delete_book(random_book_id)
    if response.status_code == 200:
        print_green(f"Book deleted with ID: {random_book_id}")
    else:
        print_red(f"Failed to delete book with ID: {random_book_id}")
