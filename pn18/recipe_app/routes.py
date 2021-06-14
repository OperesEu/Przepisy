from recipe_app import app, db
from flask import render_template, redirect, url_for
from recipe_app.forms import RegistrationForm, LoginForm
from recipe_app.models import User
from flask_login import login_user, current_user, logout_user

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)