from flask import Flask
from flask import render_template, request
#from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/heatmap")
def heatmap():
    return render_template('heatmap.html')

@app.route("/report")
def report():
    return render_template('report.html')

@app.route("/livefeed")
def livefeed():
    return render_template('livefeed.html')


if __name__ == '__main__':
    app.run()

