from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

mysql = MySQLConnector(app,'world')

@app.route('/')
def index():
    print "Hello Index"
    return render_template('index.html')

app.run(debug=True)
