#!/usr/bin/python3
"""Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """config classs"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    lang = request.args['locale']
    if lang in ['en', 'fr']:
        return lang
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', strict_slashes=False)
def index():
    """Route function"""
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run(debug=True)
