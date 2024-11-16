from library import Library
from book import Book

def main():
    # LSP features to try:
    # 1. Hover over Library to see class definition
    # 2. Code completion after typing 'library.'
    library = Library("Central Library")

    # 3. Hover over Book to see documentation
    book1 = Book(
        "1984",
        "George Orwell",
        "9780451524935"
    )

    # 4. LSP will show error if you uncomment (wrong types)
    # book2 = Book(123, [], "invalid")

    # 5. Code completion for methods
    library.add_book(book1)

    # 6. Go to definition on search_by_title
    found_book = library.search_by_title("1984")

    if found_book:
        # 7. Type annotation hints
        found_book.display_info()

if __name__ == "__main__":
    main()
