from models.books import all_books

class Book():

    @staticmethod
    def getAllBooks():
        sorted_books = sorted(all_books, key=lambda x: x['title'].lower())
        return sorted_books
    
    @staticmethod
    def getBook(bookName):
        for i in range(len(all_books)-1):
            if all_books[i]['title'] == bookName:
                print(all_books[i])
                return all_books[i]
        return None
    