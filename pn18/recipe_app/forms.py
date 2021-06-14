from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms.widgets import TextArea

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up') 

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class AddRecpieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField ('Description', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Add new')

class EditRecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField ('Description', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Save')
