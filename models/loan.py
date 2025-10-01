# import datetime as dt
from datetime import date, timedelta, datetime
import random

from app import db
from mongoengine.queryset.visitor import Q

from models.users import User
from models.booksModel import Book

class Loan(db.Document):
    meta = {"collection": "loans"}

    member = db.ReferenceField(User)
    book = db.ReferenceField(Book)

    borrowDate = db.DateField(required=True)
    returnDate = db.DateField(default = None)

    renewCount = db.IntField(default=0, min_value=0)

    @staticmethod
    def findUser(email):
        user = User.objects(email = email).first()
        return user

    @staticmethod
    def findBook(bookTitle):
        book = Book.objects(title = bookTitle).first()
        return book

    @staticmethod
    def createLoan(member,book):

        # no duplicate active loan of same book
        if Loan.objects(member=member, book=book, returnDate=None).first():
            return "You already has an active loan for this book."

        # checks availability
        if book.available <= 0:
            return "Book is not currently available."
        
        days = timedelta(days=random.randint(10,20))
        borrowDate = date.today() - days

        book.available -= 1
        book.save()
        Loan(member=member, book=book, borrowDate=borrowDate, returnDate=None, renewCount=0).save()
        return "Book was borrowed successfully."
    
    @staticmethod
    def retrieveLoans(member=None, book=None):
        q = Q()
        if member is not None:
            #finds loans for current user
            q &= Q(member=member)
        if book is not None:
            #finds loans for a specific book
            q &= Q(book=book)
        #using neither will find all loans from all users
        return Loan.objects(q).order_by("-borrowDate").select_related()
    
    @staticmethod
    def updateLoan(member, book, renew):

        bookLoan = Loan.objects(member=member, book=book, returnDate=None).first()
        if bookLoan:
            days = timedelta(days=random.randint(10,20))

            if renew and (bookLoan.renewCount < 2):
                bookLoan.renewCount += 1
                if (bookLoan.borrowDate + days) > date.today():
                    bookLoan.borrowDate = date.today()
                else:
                    bookLoan.borrowDate = bookLoan.borrowDate + days
                bookLoan.save()
                return f"Book loan has been renewed. Your new due date is {bookLoan.borrowDate}."
            
            elif (bookLoan.borrowDate + days) > date.today():
                bookLoan.returnDate = date.today()
            else:
                bookLoan.returnDate = bookLoan.borrowDate + days
            book.available += 1
            book.save()
            bookLoan.save()
            return "Book has been returned. Thank you!"
        
        return "No such book found."
    
    @staticmethod
    def deleteLoan(member, book):
        bookLoan = Loan.objects(member=member, book=book).first()
        if not bookLoan:
            return "There is no such loan to delete."
        if bookLoan.returnDate is None:
            return "Cannot delete an active loan. Return it first."
        bookLoan.delete()
        return "Book loan has been successfully deleted from your Loans."
        
