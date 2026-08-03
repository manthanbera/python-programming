# Library management system (Experiment 1)

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False

class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron_id, isbn):
        patron = None
        book = None
        for x in self.patrons:
            if x.patron_id == patron_id:
                patron = x
                break
        if patron is None:
            print("Patron not found in the system!")
            return
        
        for x in self.books:
            if x.isbn == isbn:
                book = x
                break
        if book is None:
            print("Book not found in the system!")
            return

        if patron.borrow_book(book):
            print(f"'{book.title}' borrowed by {patron.name}.")
        else:
            print(f"'{book.title}' is already borrowed by someone else.")

    def return_book(self, patron_id, isbn):
        patron = None
        for x in self.patrons:
            if x.patron_id == patron_id:
                patron = x
                break
        if patron is None:
            print("Patron not found in the system!")
            return

        book = None
        for x in self.books:
            if x.isbn == isbn:
                book = x
                break
        if book is None:
            print("Book not found in the system!")
            return

        if patron.return_book(book):
            print(f"'{book.title}' returned by {patron.name}.")
        else:
            print(f"This book was not borrowed by {patron.name}.")

