from recipe_app.forms import LoginForm
from flask import Flask
from flask.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
db = SQLAlchemy()
app = Flask(__name__)
db.init_app(app)
login_manager.init_app(app)

from recipe_app import routes