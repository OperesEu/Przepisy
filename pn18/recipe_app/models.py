from flask import render_template, request
from wtforms.validators import Email
from recipe_app.routes import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    recipe = db.relationship('recpie', backref='author', lazy=True)

class Recpie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(256), nullable=False)
    intigients = db.Column(db.Text, nullable=False)
    way = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.foreignKey('user.id'),nullable=False)
