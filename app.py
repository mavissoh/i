from flask import Flask, render_template, request, redirect, Blueprint, jsonify, url_for
from flask_mongoengine import MongoEngine, Document

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db':'ict239tma',
    'host':'localhost'
}
app.static_folder = 'assets'
db = MongoEngine(app)

from controllers.booksController import booksBlueprint

from models.booksModel import Book

import pymongo



app.register_blueprint(booksBlueprint)

# app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'auth.login'
# login_manager.login_message = "Please login or register first to get an account."



@app.route('/test')
def testing():
    return render_template('testing.html')