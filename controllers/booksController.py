from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, request, redirect, render_template, url_for

from models.forms import BookForm

# from models.users import User
from models.booksModel import Book

from flask_login import login_required
from flask import Blueprint, request, render_template

from models.forms import BookForm
from models.booksModel import Book

booksBlueprint = Blueprint('books', __name__)

genres = ["Animals", "Business", "Comics", "Communication", "Dark Academia", "Emotion", "Fantasy",
          "Fiction", "Friendship", "Graphic Novels", "Grief", "Historical Fiction", "Indigenous", "Inspirational",
          "Magic", "Mental Health", "Nonfiction", "Personal Development", "Philosophy", "Picture Books", "Poetry",
          "Productivity", "Psychology", "Romance", "School", "Self Help"]

@booksBlueprint.route('/')
@booksBlueprint.route('/books')
def home():
    category = request.args.get("category", "All")

    allBooks = Book.getAllBooks()

    if category == "All":
        filtered_books = allBooks
    else:
        filtered_books = [book for book in allBooks if book['category'] == category]

    return render_template("books.html", books=filtered_books, selected_category=category, panel='Book Titles')

@booksBlueprint.route('/books/<title>')
def bookDetails(title):
    book = Book.getBook(title)
    return render_template('bookDetails.html', book=book, panel='Book Details')

@booksBlueprint.route('/books/addBook', methods=['GET', 'POST'])
@login_required
def addBook():
    form = BookForm()
    form.genres.choices = [(g, g) for g in genres]
    
    if request.method == 'POST':
        # Handle the 'add_author' button click separately
        if "add_author" in request.form:
            form.authors.append_entry()
            return render_template('addBook.html', form=form, genres=genres, panel="Add a Book")
        
        # Handle the form submission validation
        if form.validate_on_submit():
            # Process authors list and append (Illustrator) if checked
            authors = []
            if form.authors.data is not None:
                for entry in form.authors.data:
                    name = entry.get("name", "").strip()
                    if not name:
                        continue
                    if entry.get("illustrator"):
                        name += " (Illustrator)"
                    authors.append(name)

            # Split description into list (one paragraph per line)
            description = [p.strip() for p in form.description.data.splitlines() if p.strip()]

            # Save book
            Book.createBook(
                genres=form.genres.data,
                title=form.title.data,
                category=form.category.data,
                pages=form.pages.data,
                copies=form.copies.data,
                available=form.copies.data,
                authors=authors,
                url=form.url.data,
                description=description
            )
            return redirect(url_for('books.home'))

    if request.method == 'POST' and not form.validate():
        print("Form errors:", form.errors)  # or flash them
        
    # If it's a GET request or a failed POST, ensure at least one author field exists
    if len(form.authors.entries) == 0:
        form.authors.append_entry()


    return render_template('addBook.html', form=form, genres=genres, panel="Add a Book")

