#!/usr/bin/python3
"""
1. This script opens a Flask web application
"""


from flask import Flask
from flask import escape


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    return 'HBNB'


@app.route('/c/<text>')
def show_user_profile(text):
    # show the user profile for that user
    return 'C %s' % escape(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
