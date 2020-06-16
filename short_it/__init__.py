from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    'db': 'shortit',
    'host': 'mongodb://localhost/shorit'
}
db = MongoEngine(app)


from short_it import routes