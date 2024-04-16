from BookService import BookService
from BookEntity import Book

class BookController:
    # # 생성자
    # def __init__(self):
    #     print(self) # self = this (자기자신의 주소값)

    @classmethod
    def addBookRequest(cls):
        book = Book(
            bookName="테스트 도서명", 
            authorName="테스트 저자명", 
            publisherName="테스트 출판사명", 
            isbn="1234"
        )
        BookService.addBook()