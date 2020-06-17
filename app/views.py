from flask import render_template

from app import app

@app.route('/')
def index():
	return "Hello World! This is my first deployed app"

@app.route('/<name>')
def about():
	return "Hello " + name;
