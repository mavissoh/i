from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FieldList, IntegerField, SelectMultipleField, BooleanField, SelectField, FormField, TextAreaField
from wtforms.validators import Email, Length, InputRequired

class RegForm(FlaskForm):
    email = StringField('Email',  validators=[InputRequired(), Email(message='Invalid email')])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=20)])
    name = StringField('Name')

class AuthorForm(FlaskForm):
    # disable CSRF for this nested subform
    class Meta:
        csrf = False

    name = StringField("Author")
    illustrator = BooleanField("Illustrator")

class BookForm(FlaskForm):
    genres = SelectMultipleField("Choose multiple Genres:", validators=[InputRequired()])
    title = StringField("Title:", validators=[InputRequired()])
    category = SelectField("Choose a category:", choices=[("Children","Children"),("Teens","Teens"),("Adult","Adult")])
    pages = IntegerField("Number of Pages:", validators=[InputRequired()])
    copies = IntegerField("Number of Copies:", validators=[InputRequired()])
    url = StringField("URL for Cover:", validators=[InputRequired()])
    description = TextAreaField("Description:", validators=[InputRequired()])
    
    # Unlimited authors
    authors = FieldList(FormField(AuthorForm), min_entries=1)

