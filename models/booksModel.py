from models.books import all_books
from app import db

class Book(db.Document):
    meta = {'collection': 'allBooks'}
    genres = db.ListField()
    title = db.StringField()
    category = db.StringField()
    pages = db.IntField()
    copies = db.IntField()
    available = db.IntField()
    authors = db.ListField()
    url = db.StringField()
    description = db.ListField()

    @staticmethod
    def addBooks():
        if Book.objects.count() == 0:
            for item in all_books:
                Book.createBook(
                    item['genres'], item['title'], item['category'], item['pages'], item['copies'], 
                    item['available'], item['authors'], item['url'], item['description'])

    @staticmethod
    def createBook(genres, title, category, pages, copies, available, authors, url, description):
        return Book(genres=genres, title=title, category=category, pages=pages, copies=copies, 
                    available=available, authors=authors, url=url, description=description).save()


    @staticmethod
    def getAllBooks():
        Book.addBooks()
        sorted_books = sorted(Book.objects(), key=lambda x: x['title'].lower())
        return sorted_books
    
    @staticmethod
    def getBook(bookName):
        return Book.objects(title = bookName).first()
    
    @staticmethod
    def borrowBook(bookName):
        book = Book.objects(title = bookName).first()
        if book:
            if book.available >= 1:
                book.available -= 1
                return book.save()
        return "Loan unsuccessful"
    
    @staticmethod
    def returnBook(bookName):
        book = Book.objects(title = bookName).first()
        if book:
            if book.available < book.copies:
                book.available += 1
                return book.save()
        return "Return unsuccessful"
            
    