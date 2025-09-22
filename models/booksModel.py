from models.books import all_books

# print(all_books[0]['title'])

# all_books is list of dictionaries
# all_books[0] is the first book in the list
# all_books[0]['genres'] is the list of genres in the first book
# all_books[0]['genres'][0] is the first genre in the list of genres

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
    
# Book.getBook('this book doesnt exist')
# Book.getBook('The Day the Books Disappeared')