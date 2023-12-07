# test_library_system.py
import pytest
from library_system import Book, Library

@pytest.fixture
def library_with_books():
    library = Library()
    book1 = Book("Book1", "Author1", 2)
    book2 = Book("Book2", "Author2", 5)
    library.books = [book1, book2]
    return library

def test_checkout_books(library_with_books):
    selected_books = [Book("Book1", "Author1", 2), Book("Book2", "Author2", 3)]
    total_late_fee = library_with_books.checkout_books(selected_books)
    assert total_late_fee == 0
    assert library_with_books.books[0].quantity == 0
    assert library_with_books.books[1].quantity == 2

def test_return_books(library_with_books):
    selected_books = [Book("Book1", "Author1", 2), Book("Book2", "Author2", 3)]
    library_with_books.checkout_books(selected_books)

    returned_books = [Book("Book1", "Author1", 1), Book("Book2", "Author2", 2)]
    total_late_fee = library_with_books.return_books(returned_books)

    # La cantidad devuelta debería ser 1 para Book1 y 2 para Book2
    assert library_with_books.books[0].quantity == 1
    assert library_with_books.books[1].quantity == 3

    # La tarifa por demora debería ser 2
    assert total_late_fee == 2