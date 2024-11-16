from typing import List, Optional
from book import Book

class Library:
    """
    A class representing a library that manages a collection of books.

    Attributes:
        name (str): The name of the library
        books (List[Book]): List of books in the library
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """
        Add a book to the library.

        Args:
            book (Book): The book to add
        """
        self.books.append(book)

    def search_by_title(self, title: str) -> Optional[Book]:
        """
        Search for a book by its title.

        Args:
            title (str): The title to search for

        Returns:
            Optional[Book]: The found book or None
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_inventory(self) -> None:
        """Display all books in the library."""
        print(f"\nInventory of {self.name}:")
        for book in self.books:
            book.display_info()

