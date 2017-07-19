from flask import Flask
from flask import render_template, request
import sqlite3 as sql
#from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os


DATABASE = 'test.db'

app = Flask(__name__)
app.debug = True

def get_alerts():
    with sql.connect("test.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM alerts")
        data = cur.fetchall()
    return data

 
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
    data = get_alerts()
    return render_template('livefeed.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/alert_handler', methods = ['POST', 'GET'])
def alert_handler():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        time = request.form['time']

        with sql.connect("test.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO alerts (name, time, location) VALUES (?,?,?)", (name, time, location))
            con.commit()

        return render_template("alertbutton.html")
        con.close()
         

if __name__ == '__main__':
    app.run()

