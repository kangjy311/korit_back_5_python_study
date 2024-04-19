class Book:

    def __init__(self, bookId, bookName, author, publisher):
        self.bookId = bookId
        self.bookName = bookName
        self.author = author
        self.publisher = publisher

    def __str__(self):
        return f"""
번호: {self.bookId}
도서명: {self.bookName}
저자: {self.author}
출판사: {self.publisher}
"""
        
if __name__ == "__main__":
    book = Book(
        1,
        "혼자 공부하는 머신러닝+딥러닝",
        "박해선",
        "한빛미디어"
    )
print(book)

