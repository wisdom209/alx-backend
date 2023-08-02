#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """config class to configure available languages"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """get the locale lang"""
    lang = request.args.get("locale")
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(login_as):
    """return user dict"""
    if not login_as:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    """pre hook before request"""
    login_as = request.args.get("login_as")
    g.user = get_user(login_as)


@app.route('/', strict_slashes=False)
def index():
    """route index"""
    username = None
    print(f"user {g.user}")
    if g.user:
        username = g.user.get('name')
    return render_template('5-index.html', username=username)


if __name__ == "__main__":
    app.run(debug=True)
