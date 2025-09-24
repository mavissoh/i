from flask import Flask, render_template, request, redirect, Blueprint, jsonify, url_for
from flask_mongoengine import MongoEngine, Document

from controllers.booksController import booksBlueprint

from models.booksModel import Book

import pymongo
import csv
import io
import json
import datetime as dt
import os

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db':'ict239tma',
    'host':'localhost'
}
app.static_folder = 'assets'
db = MongoEngine(app)

app.register_blueprint(booksBlueprint)

@app.route('/test')
def testing():
    return render_template('testing.html')