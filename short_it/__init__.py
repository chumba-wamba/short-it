from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine
from flask_login import LoginManager


app = Flask(__name__) # Initializing flask app
app.config["MONGODB_SETTINGS"] = {
    'db': 'shortit',
    'host': 'mongodb://localhost/shortit'
} # Configuring flask app to store MongoDB 
# host and db_name
app.config['SECRET_KEY'] = "SECRET_KEY" # Initializing flask secret key
db = MongoEngine(app) # Initializing flask mongonengine
bcrypt = Bcrypt(app) # Initializing flask bcrypt
login_manager = LoginManager(app) # Initializing flask login

login_manager.login_view = "login" # Initializing login route
login_manager.login_message_category = "info" # intializing flash message category for login required

from short_it import routes