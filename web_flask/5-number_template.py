#!/usr/bin/python3
"""
1. This script opens a Flask web application
"""


from flask import Flask
from flask import escape
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    # show the text Hello HBNB if root
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    # show the text HBNB if folder /hbnb
    return 'HBNB'


@app.route('/c/<text>')
def show_c_is_(text):
    # show the text C is <text> if route /c/<text>
    return 'C %s' % escape(text.replace("_", " "))


@app.route('/python/<text>')
def show_python_is_1(text):
    # show the text Python is <text> if route /python/<text>
    return 'Python %s' % escape(text.replace("_", " "))


@app.route('/python')
def show_python_is_2(text='is cool'):
    # show the text Python is cool if route /python or route /pyhton/
    return 'Python %s' % escape(text.replace("_", " "))


@app.route('/number/<int:n>')
def show_n_is_number(n):
    # show if n is number the text n is a number
    return '%d is a number' % n

@app.route('/number_template/<int:n>')
def show_n_number_template(n):
    # show if n is number the text n is a number
    return render_template('/5-number.html', n = n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
