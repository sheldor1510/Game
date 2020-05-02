from flask import Flask
from flask import render_template, url_for, redirect
import random
app = Flask(__name__)




@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
@app.route('/main')
def main():
    return render_template('layout.html')


@app.route('/another')
def another():
    return render_template('another.html')


@app.route('/result1')
def result1():
    fem = ["Paper","Rock","Scissors"]
    com = random.choice(fem)
    if com == "Paper":
        return render_template('result.html', choice=com, result="lost")
    elif com == "Rock":
        return render_template('result.html', choice=com, result="drawed")
    elif com == "Scissors":
        return render_template('result.html', choice=com, result="won")

@app.route('/result2')
def result2():
    fem = ["Paper","Rock","Scissors"]
    com = random.choice(fem)
    if com == "Paper":
        return render_template('result.html', choice=com, result="drawed")
    elif com == "Rock":
        return render_template('result.html', choice=com, result="won")
    elif com == "Scissors":
        return render_template('result.html', choice=com, result="lost")

@app.route('/result3')
def result3():
    fem = ["Paper","Rock","Scissors"]
    com = random.choice(fem)
    if com == "Paper":
        return render_template('result.html', choice=com, result="won")
    elif com == "Rock":
        return render_template('result.html', choice=com, result="lost")
    elif com == "Scissors":
        return render_template('result.html', choice=com, result="drawed")


    

if __name__ == '__main__':
    app.run(debug=True)