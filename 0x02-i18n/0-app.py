#!/usr/bin/env python3
"""A basic flask app"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """index route function"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
