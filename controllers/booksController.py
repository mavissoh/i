from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, request, redirect, render_template, url_for

# from models.forms import BookForm

# from models.users import User
from models.booksModel import Book

booksBlueprint = Blueprint('books', __name__)

@booksBlueprint.route('/')
@booksBlueprint.route('/books')
def home():
    category = request.args.get("category", "All")

    allBooks = Book.getAllBooks()
    
    if category == "All":
        filtered_books = allBooks
    else:
        filtered_books = [book for book in allBooks if book['category'] == category]

    return render_template("books.html", books=filtered_books, selected_category=category, panel = 'Book Titles')

@booksBlueprint.route('/books/<title>')
def bookDetails(title):
    book = Book.getBook(title)
    return render_template('bookDetails.html', book=book, panel='Book Details')
