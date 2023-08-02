#!/usr/bin/python3
"""Flask app"""
from flask import Flask, render_template, request, g, session
from flask_babel import Babel, gettext as _


class Config:
    """config classs"""
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


def get_user(login_as):
    """get a user"""
    if login_as is None:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    """Before a request"""
    login_as = request.args.get('login_as')
    g.user = get_user(login_as)


@babel.localeselector
def get_locale():
    """get locale"""
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', strict_slashes=False)
def index():
    """Route function"""
    username = None
    if g.user:
        username = g.user.get('name')
    return render_template("5-index.html", username=username)


if __name__ == '__main__':
    app.run(debug=True)
