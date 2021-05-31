from flask import Flask, render_template,  url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, AddRecpieForm, RegistrationForm
from flask_login import login_user, current_user, logout_user, login_required
app = Flask(__name__)

db = SQLAlchemy()

@app.route('/')
def hello_world():
    user=LoginForm.username
    return render_template("Register.html", user=user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        password = password(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)