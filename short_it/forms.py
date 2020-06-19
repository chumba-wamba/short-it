from flask_wtf import FlaskForm
from short_it.models import URL, User
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    user_name = StringField(label="Username", validators=[
                            DataRequired(), Length(min=6, max=20)])
    password = PasswordField(label="Password", validators=[
                             DataRequired(), Length(min=6, max=20)])
    login = SubmitField(label="Login")


class RegistrationForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[
                             DataRequired(), Length(max=20)])
    last_name = StringField(label="Last Name", validators=[
                            Length(max=20)])
    user_name = StringField(label="Username", validators=[
                            DataRequired(), Length(min=6, max=20)])
    email = StringField(label="Email", validators=[
                        DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[
                             DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField(label="Confirm Password", validators=[
                                     DataRequired(), EqualTo("password")])
    register = SubmitField(label="Register")

    def validate_user_name(self, user_name):
        object_list = User.objects(user_name=user_name.data)
        if len(object_list) > 0:
            raise ValidationError("The user name is already taken.")

    def validate_email(self, email):
        object_list = User.objects(email=email.data)
        if len(object_list) > 0:
            raise ValidationError("The email is already taken.")


class ShortenForm(FlaskForm):
    original_url = URLField(label="Original URL", validators=[DataRequired()])
    shortened_url = StringField(label="Keyword")
    shorten = SubmitField(label="Short It!")

    def validate_shortened_url(self, shortened_url):
        object_list = User.objects(shortened_url=shortened_url.data)
        if len(object_list) > 0:
            raise ValidationError("The shortened url is already taken.")
