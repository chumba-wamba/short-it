from flask_login import UserMixin
from datetime import datetime
from short_it import db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.objects(id=id).first()


class URL(db.Document):
    original_url = db.StringField(required=True)
    shortened_url = db.StringField(unique=True, required=True)
    date_defined = db.DateTimeField(default=datetime.utcnow)
    counter = db.IntField(default=0)
    date_array = db.ListField(db.DateTimeField())
    owner = db.ObjectIdField(default=None)

    # def __repr__(self):
    #     return f"original url: {self.original_url}, shortened url: {self.shortened_url}, owner: {self.owner}"


class User(UserMixin, db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=False)
    user_name = db.StringField(unique=True, required=True)
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    shared_url_list = db.ListField()

    def __repr__(self):
        return f"user_name: {self.user_name}, url_list: {self.url_list}"
