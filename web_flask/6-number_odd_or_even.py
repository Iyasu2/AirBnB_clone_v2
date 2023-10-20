#!/usr/bin/python3
'''
this module starts a basic application
'''
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    '''
    this function returns a text
    '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    '''
    this function returns a text
    '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def input(text):
    '''
    this function returns a text
    '''
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/", defaults={'text2': 'is cool'}, strict_slashes=False)
@app.route("/python/<text2>", strict_slashes=False)
def input_python(text2):
    '''
    this function returns a text
    '''
    text2 = text2.replace('_', ' ')
    return f"Python {text2}"


@app.route("/number/<int:n>", strict_slashes=False)
def input_number(n):
    '''
    this function returns a text
    '''
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    '''
    this function returns a text
    '''
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even_template(n):
    '''
    this function returns a text
    '''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
