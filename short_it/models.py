from datetime import datetime
from short_it import db


class URL(db.Document):
    original_url = db.StringField(required=True)
    shortened_url = db.StringField(unique=True, required=True)
    date_defined = db.DateTimeField(default=datetime.utcnow)
    counter = db.IntField(default=0)
    date_array = db.ListField(db.DateTimeField())


class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=False)
    user_name = db.StringField(unique=True, required=True)
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    url_list = db.ListField(URL())
