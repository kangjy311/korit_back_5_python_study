bookDic1 = {}
bookDic2 = {}
bookDic3 = {}
bookList = []

bookDic1 = {
    "bookName": "Do it! 점프 투 파이썬",
    "author": "박응용",
    "publisher": "이지스퍼블리싱"
}
bookDic2 = {
    "bookName": "혼자 공부하는 파이썬",
    "author": "윤인성",
    "publisher": "한빛미디어"
}
bookDic3 = {
    "bookName": "챗GPT API를 활용한 챗봇 만들기",
    "author": "이승우",
    "publisher": "한빛미디어"
}
bookList.append(bookDic1)
bookList.append(bookDic2)
bookList.append(bookDic3)

for book in bookList:
    print("저자명 :" ,book["bookName"])
    print("저자 :" ,book["author"])
    print("출판사 :" ,book["publisher"])
    print()