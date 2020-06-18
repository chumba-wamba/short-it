from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    user_name = StringField(label="Username", validators=[
                            DataRequired(), Length(min=6, max=20)])
    password = PasswordField(label="Password", validators=[
                             DataRequired(), Length(min=6, max=20)])
    login = SubmitField(label="Login")


class RegistrationForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[
                             DataRequired(), Length(min=6, max=20)])
    last_name = StringField(label="Last Name", validators=[
                            Length(min=6, max=20)])
    user_name = StringField(label="Username", validators=[
                            DataRequired(), Length(min=6, max=20)])
    email = StringField(label="Email", validators=[
                        DataRequired(), Length(min=6, max=20)])
    password = PasswordField(label="Password", validators=[
                             DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField(label="Confirm Password", validators=[
                                     DataRequired(), EqualTo("password")])
    register = SubmitField(label="Register")
