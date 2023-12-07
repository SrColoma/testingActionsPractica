# library_system.py
import datetime

class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity
        self.due_date = None

class Library:
    def __init__(self):
        self.books = []

    def display_catalog(self):
        for book in self.books:
            print(f"{book.title} by {book.author} - Available: {book.quantity}")

    def checkout_books(self, selected_books):
        total_late_fee = 0

        for selected_book in selected_books:
            for library_book in self.books:
                if (
                    library_book.title == selected_book.title
                    and library_book.author == selected_book.author
                ):
                    if selected_book.quantity > 0 and selected_book.quantity <= 10:
                        if selected_book.quantity <= library_book.quantity:
                            library_book.quantity -= selected_book.quantity
                            selected_book.due_date = (
                                datetime.date.today()
                                + datetime.timedelta(days=14)
                            )
                        else:
                            print(
                                f"Error: Not enough copies available for {selected_book.title}"
                            )
                            return -1
                    else:
                        print(
                            f"Error: Invalid quantity for {selected_book.title}"
                        )
                        return -1

        return total_late_fee  # Actualizar la devolución de total_late_fee


def return_books(self, returned_books):
    total_late_fee = 0

    for returned_book in returned_books:
        for library_book in self.books:
            if (
                returned_book.title == library_book.title
                and returned_book.author == library_book.author
            ):
                if returned_book.quantity <= library_book.quantity:
                    library_book.quantity += returned_book.quantity
                    returned_book.quantity = 0
                    returned_book.due_date = None
                    # Calcular la tarifa por demora si la fecha de vencimiento ha pasado
                    if returned_book.due_date and datetime.date.today() > returned_book.due_date:
                        days_overdue = (
                            datetime.date.today() - returned_book.due_date
                        ).days
                        late_fee = days_overdue * 1
                        total_late_fee += late_fee
                else:
                    print(
                        f"Error: Returned quantity exceeds the quantity borrowed for {returned_book.title}"
                    )
                    return -1

    return total_late_fee

