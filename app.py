from flask import Flask, render_template, request, redirect
from models.booksModel import Book

app = Flask(__name__)

app.static_folder = 'assets'

@app.route('/')
@app.route('/books')
def home():
    category = request.args.get("category", "All")

    allBooks = Book.getAllBooks()
    
    if category == "All":
        filtered_books = allBooks
    else:
        filtered_books = [book for book in allBooks if book['category'] == category]

    return render_template("books.html", books=filtered_books, selected_category=category, panel = 'Book Titles')

@app.route('/books/<title>')
def bookDetails(title):
    book_title = Book.getBook(title)
    return render_template('bookDetails.html', bookTitle=book_title, panel='Book Details')

@app.route('/test')
def testing():
    return render_template('testing.html')