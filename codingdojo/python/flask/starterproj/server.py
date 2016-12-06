from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    print "Hello2"
    return render_template('index.html')

@app.route('/roll', methods=["POST"])
def roll():
    print "Hello"

    return redirect('/')




app.run(debug=True)
