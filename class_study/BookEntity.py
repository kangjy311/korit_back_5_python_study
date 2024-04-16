class Book:

    def __init__(self, bookId=0, bookName="", authorName="", publisherName="", isbn=""):
        self.bookId = bookId
        self.bookName = bookName
        self.authorName = authorName
        self.publisherName = publisherName
        self.inbn = isbn

    def setAuthor(self, author):
        self.author = author

    def __str__(self):
        # 따옴표 """  """ 세개 쓰면 줄바꿈 할 수 있음
        # f"(문자열안에) {} "": 중괄호 안에 값 대입 가능
        return f"""Book[
bookId: {self.bookId}
bookName: {self.bookName}
authorName: {self.authorName}
publisherName: {self.publisherName}]"""
        # return "Book[bookId: {bookId}, bookName: {bookName}]".format(bookId = self.bookId, bookName = self.bookName)
        # return "Book[bookId: %d, bookName: %s]" % (self.bookId, self.bookName)
        