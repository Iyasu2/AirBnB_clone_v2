#!/usr/bin/python3
'''
this module starts a basic application
'''
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    '''
    this function returns a text
    '''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
