from flask import Flask

# Config imports
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import for Flask Login
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app,db)

# Login Flow config
login = LoginManager(app)
login.login_view = 'login' # This specifies that page to load for non0 authorized users 


from fantasy_guru import routes, models 

# Once we have a __init__.py; the whole folder becomes a package and everything else is apart of it