#!/usr/bin/python3
"""
1. This script opens a Flask web application
"""


from flask import Flask
from flask import escape
from flask import render_template


from models import storage, State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ list the states of HBNB"""
    state_dict = storage.all(State).values()
    return render_template('7-states_list.html', state_dict=state_dict)


@app.teardown_appcontext
def state_close(error):
    """ close the connection"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
