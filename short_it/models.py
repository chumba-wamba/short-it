from flask_login import UserMixin
from datetime import datetime
from short_it import db, login_manager


# This block of code helps the login manager
# acquire the id of the current user from
# the User model in the database
@login_manager.user_loader
def load_user(id):
    return User.objects(id=id).first()


# Class for the URL model
# The fields are self explanatory
class URL(db.Document):
    original_url = db.StringField(required=True)
    shortened_url = db.StringField(unique=True, required=True)
    date_defined = db.DateTimeField(default=datetime.utcnow)
    counter = db.IntField(default=0)
    date_array = db.ListField(db.DateTimeField())
    owner = db.ObjectIdField(default=None)

    def __repr__(self):
        return f"original url: {self.original_url}, shortened url: {self.shortened_url}, owner: {self.owner}"


# Class for the User model
# The fields are self explanatory
# The UserMixin inheritance is a part of the
# login manager to allow for certain important
# methods to be a part of this class
# The login manager is dependant on these
# essential methods for its working
class User(UserMixin, db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=False)
    user_name = db.StringField(unique=True, required=True)
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    shared_url_list = db.ListField()

    def __repr__(self):
        return f"user_name: {self.user_name}, url_list: {self.url_list}"
