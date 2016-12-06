import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    print "Hello Index"
    return render_template('index.html')

@app.route('/roll', methods=["POST"])
def roll():
    print "Hello after submit"
    fname = request.form['name']
    typeofdice = int(request.form['typeofdice'])
    numberofdice = int(request.form['numberofdice'])
    diceresult=0
    result=0
    flag = 0
    for i in range(numberofdice):
        while flag is 0:
            dicetoss = random.random()
            diceresult = int(dicetoss * 10)
            if diceresult > 0 and diceresult <= typeofdice:
                flag = 1
                print diceresult
        result = result + diceresult
        flag=0

    return render_template('roll.html',name=fname, results=result, td=typeofdice, nd=numberofdice )

@app.route('/ninjas')
def ninjas():
    print "Hello after submit"
    return render_template('yb.html')

@app.route('/dojos/new')
def dojos():
    print "Hello after submit"
    return render_template('index.html')

app.run(debug=True)
