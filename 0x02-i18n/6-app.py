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
    """select the best match for supported languages"""
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        print(f"locale {locale}")
        return locale
    user_locale = g.user.get('locale')
    if user_locale in app.config['LANGUAGES']:
        print(f"user_locale {user_locale}")
        return user_locale
    b_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if b_locale in app.config['LANGUAGES']:
        print(f"browser_locale {b_locale}")
        return b_locale
    return "en"


def get_user(login_as):
    """function that returns a user dictionary or None if th ID is not found"""
    user_id = int(login_as) if login_as else None
    if user_id in users:
        return users[user_id]
    return None


@app.before_request
def before_request():
    """use get_user to find a user if any"""
    login_as = request.args.get("login_as")
    g.user = get_user(login_as)


@app.route('/', strict_slashes=False)
def index():
    """index function"""
    username = None
    if g.user:
        username = g.user.get('name')
    return render_template('6-index.html', username=username)


if __name__ == "__main__":
    app.run(debug=True)
