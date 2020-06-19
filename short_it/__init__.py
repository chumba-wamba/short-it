from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine
from flask_login import LoginManager


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    'db': 'shortit',
    'host': 'mongodb://localhost/shortit'
}
app.config['SECRET_KEY'] = "SECRET_KEY"
db = MongoEngine(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = "login"
login_manager.login_message_category = "info"

from short_it import routes