class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_pages(self):
        return self.__pages

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Error")

    def is_available(self):
        return self.__available

    def borrow(self):
        if self.is_available():
            self.__available = False
        else:
            print("Not available")

    def return_book(self):
        if not self.is_available():
            self.__available = True
        else:
            print("Not borrow")


book = Book("Harry","Mac", 50)

book.borrow()
book.return_book()
