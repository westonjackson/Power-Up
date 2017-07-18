from flask import Flask
from flask import render_template, request
import sqlite3
#from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os

DATABASE = 'test.db'

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/alertbutton')
def alertbutton():
    return render_template('alertbutton.html')

@app.route("/heatmap")
def heatmap():
    return render_template('heatmap.html')

@app.route("/report")
def report():
    return render_template('report.html')

@app.route("/livefeed")
def livefeed():
    return render_template('livefeed.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/about')
def about():
    return render_template('about.html')






if __name__ == '__main__':
    app.run()

