from flask_wtf import FlaskForm
from short_it.models import URL, User
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, Optional


# Stackoverflow code for optional validation;
# This works in such a manner that when a field
# passed as argument within RequiredIf is appended
# to the validators list of some other field, than
# the validaton is invoked when the argument field
# is non-empty.
class RequiredIf(InputRequired):
    field_flags = ('requiredif',)

    def __init__(self, other_field_name, message=None, *args, **kwargs):
        self.other_field_name = other_field_name
        self.message = message

    def __call__(self, form, field):
        other_field = form[self.other_field_name]
        if other_field is None:
            raise Exception('no field named "%s" in form' %
                            self.other_field_name)
        if bool(other_field.data):
            super(RequiredIf, self).__call__(form, field)
        else:
            Optional().__call__(form, field)


# Class for the login form present within the
# login route 
# The fields are self explanatory
class LoginForm(FlaskForm):
    user_name = StringField(label="Username", validators=[
                            DataRequired(), Length(min=6, max=20)])
    password = PasswordField(label="Password", validators=[
                             DataRequired(), Length(min=6, max=20)])
    login = SubmitField(label="Login")


# Class for the registration form present within the
# register route 
# The fields are self explanatory
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


# Class for the shorten form present within the
# shorten route 
# The fields are self explanatory
class ShortenForm(FlaskForm):
    original_url = URLField(label="Original URL", validators=[DataRequired()])
    shortened_url = StringField(label="Keyword")
    shorten = SubmitField(label="Short It!")

    def validate_shortened_url(self, shortened_url):
        if shortened_url.data:
            object_list = URL.objects(shortened_url=shortened_url.data)
            if len(object_list) > 0:
                raise ValidationError("The shortened url is already taken.")


# Class for the share form present within the
# share route 
# The fields are self explanatory
# This form is used by the owners of shortened URLS
# to share the dashboard of to other users
class ShareForm(FlaskForm):
    user_name = StringField("Username", validators=[
                            DataRequired()])
    share = SubmitField("Share")


# Class for the account form present within the
# account route 
# The fields are self explanatory
# Helps in updating account information such as 
# first name, last name, and password
class AccountForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[Length(max=20)])
    last_name = StringField(label="Last Name", validators=[Length(max=20)])
    password = PasswordField(label="Original Password")
    new_password = PasswordField(label="New Password", validators=[
                                 RequiredIf("password"), Length(min=6, max=20)])
    confirm_new_password = PasswordField(label="Confirm New Password", validators=[
        RequiredIf("new_password"), EqualTo("new_password")])
    update = SubmitField(label="Update")

    def validate_email(self, email):
        object_list = User.objects(email=email.data)
        if len(object_list) > 0:
            raise ValidationError("The email is already taken.")
