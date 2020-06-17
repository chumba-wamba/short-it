from datetime import datetime
from short_it import db


class URL(db.Document):
    shortened = db.StringField(unique=True, required=True)
    URL = db.StringField(required=True)
    date_defined = db.DateTimeField(default=datetime.utcnow)
    counter = db.IntField(default=0)
    date_array = db.ListField(db.DateTimeField())


class User(db.Document):
    user_name = db.StringField(unique=True, required=True)
    email = db.EmailField(unique=True, required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=False)
