from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__checked_out_books = []
        self.__checked_in_books = []

    # Getters
    def get_books(self) -> list:
        return self.__books

    def get_users(self) -> list:
        return self.__users

    def get_checked_out_books(self) -> list:
        return self.__checked_out_books

    def get_checked_in_books(self) -> list:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn, title, author) -> None:
        self.__books.append(Book(isbn,title, author))


    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}")

    # 2.1 Check out book
    def check_out_book(self, isbn, dni, due_date) -> str:
        feedback_text: str = ""
        has_book: bool = False
        has_user: bool = False
        available: bool = False
        for book in self.__books:
            
            if book[0] == isbn: 
                has_book = True
                available = book[3]

        for user in self.__users:
            if user[0] == dni:
                has_user = True
        
        if has_book and has_user:
            if available:
                feedback_text = f"User {dni} checked out book {isbn}"
            else:
                feedback_text = f"Book {isbn} is not available"    
        else:
            feedback_text = f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"
        
        return feedback_text
        

    # 2.2 Check in book
    def check_in_book(self, isbn, dni, returned_date) -> str:

        for book in self.__books:
            if book[0] == isbn and not book[3]:
                book[3] = True
                self.__checked_in_books.append(book)
        for user in self.__users:
            if user[0] == dni:
                user[3] += 1

        return f"Book {isbn} is not available"

        

    # Utils
    def add_user(self, dni, name) -> None:
        pass
