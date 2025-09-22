from flask import Flask, render_template, request, redirect
from models.booksModel import Book

app = Flask(__name__)

app.static_folder = 'assets'

@app.route('/')
@app.route('/books')
def home():
    all_books = Book.getAllBooks()
    return render_template('books.html', panel="Book Titles", books=all_books)

@app.route('/books/<title>')
def bookDetails(title):
    book_title = Book.getBook(title)
    return render_template('bookDetails.html', bookTitle=book_title, panel='Book Details')

@app.route('/test')
def testing():
    return render_template('testing.html')