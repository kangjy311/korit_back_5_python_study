import pymysql
import pymysql.cursors

class BookDB:

    host = "localhost"
    port = 3306
    user = "admin"
    password = "1234"
    database = "book_db"

    def __init__(self, bookId, bookName, author, publisher):
        self.bookId = bookId
        self.bookName = bookName
        self.author = author
        self.publisher = publisher

    bookDict = {
        "bookName": "Hey, 파이썬! 생성형 AI 활용 앱 만들어 줘",
        "author": "김한호, 최태온, 윤택한",
        "publisher": "성안당"
    }

    @classmethod
    def saveBook(cls, book=None):
        connection = pymysql.connect(
            host=cls.host,
            port=cls.port,
            user=cls.user,
            password=cls.password,
            database=cls.database    
        )

        
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = f'''
            insert into book_tb
            values (0,
                %s,
                %s,
                %s
            )
        '''
        cursor.excute(sql, (book.bookName, book.authorName, book.publisherName))
        connection.commit()