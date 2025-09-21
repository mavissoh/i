from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.static_folder = 'assets'

@app.route('/')
def home():
    return render_template('base.html')