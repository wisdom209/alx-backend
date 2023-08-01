#!/usr/bin/python3
"""Flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class config:
    """config classs"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return config.LANGUAGES[0]


@app.route('/', strict_slashes=False)
def index():
    """Route function"""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(debug=True)
