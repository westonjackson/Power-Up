from flask import Flask
from flask import render_template, request, redirect, url_for
import sqlite3 as sql
#from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os


DATABASE = 'database.db'

app = Flask(__name__)
app.debug = True

def get_pins():
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("SELECT latitude, longitude FROM alerts")
        data = cur.fetchall()
    return data
  

def get_alerts():
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("SELECT name, time, location, description FROM alerts")
        data = cur.fetchall()
    return data

 
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/heatmap")
def heatmap():
    data = get_pins()
    return render_template('heatmap.html', data=data)

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
        description = request.form['description']

                

        with sql.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO alerts (name, time, location, latitude, longitude, description) VALUES (?,?,?,?,?,?)", (name, time, location, latitude, longitude, description))
            con.commit()
        
        con.close()
        return redirect(url_for('livefeed'))
        
         

if __name__ == '__main__':
    app.run()

