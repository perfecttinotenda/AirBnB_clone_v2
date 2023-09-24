#!/usr/bin/python3
""" Will start my Flask web app """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """rtrn or (answer) Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
