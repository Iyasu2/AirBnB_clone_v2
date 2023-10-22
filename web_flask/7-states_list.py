#!/usr/bin/python3
'''
this module starts a basic application
'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def dispose(exception):
    '''
    Remove current session
    '''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    '''
    Display list of states
    '''
    states = storage.all(State)
    states_list = list(states.values())
    return render_template('7-states_list.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
