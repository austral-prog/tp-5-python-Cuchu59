class Book:
    def init(self, isbn: str, title: str, author: str, available: bool = True, checkout_num: int = 0) -> None:
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.available: bool = available
        self.checkout_num: int = checkout_num

    # Getters
    def get_isbn(self) -> str:
        return self.isbn

    def get_title(self) -> str:
        return self.title

    def get_author(self) -> str:
        return self.author

    def is_available(self) -> bool:
        return self.available

    def get_checkout_num(self) -> int:
        return self.checkout_num

    # Setters
    def set_available(self, available: bool) -> None:
        self.available = available

    def increment_checkout_num(self) -> None:
        self.checkout_num += 1

    # Utils
    def str(self) -> str:
        return (f"ISBN: {self.isbn}, Title: {self.title}, "
                f"Author: {self.author}, Available: {self.available}, "
                f"Checkout Number: {self.checkout_num}")

    def eq(self, other: object) -> bool:
        if isinstance(other, Book):
            return (self.isbn == other.isbn and
                    self.title == other.title and
                    self.author == other.author and
                    self.available == other.available and
                    self.checkout_num == other.__checkout_num)
        return False
