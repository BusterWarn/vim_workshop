class Book:
    """
    A class representing a book.

    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        isbn (str): The ISBN of the book
    """

    def __init__(self, title: str, author: str, isbn: str) -> None:
        """
        Initialize a new book.

        Args:
            title (str): The title of the book
            author (str): The author of the book
            isbn (str): The ISBN of the book
        """
        if not all([title, author, isbn]):
            raise ValueError("All fields must be non-empty")

        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self) -> None:
        """Display the book's information."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print("-" * 20)
