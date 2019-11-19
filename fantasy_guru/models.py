'''
    Models.py is where I created my database "tables" AKA models.
    Which are python Objects that will be mapped to tables when a migration 
    happens.

    - Migration: Taking a Object in python(AKA class) and relating that object to
    SQL code that is written from our python code.
'''

from flask_sqlalchemy import SQLAlchemy 
from fantasy_guru import app,db
from werkzeug.security import generate_password_hash,check_password_hash

#Import for Date Time
from datetime import datetime

# User Auth Flow Mixin 
from flask_login import UserMixin 

# Import login_manager
from fantasy_guru import login

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# One to Many Relationships
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True) # main identifier for our user table
    username = db.Column(db.String(150), nullable = False) # Telling our database that this CANNOT be empty when we say nullable = False
    email = db.Column(db.String(150), unique = True, nullable = False) # Telling our database that this has to be different each time when we say unique = True and that this cannot be empty either
    password = db.Column(db.String(256), nullable = False) # Telling our database that this CANNOT be empty when we say nullable = False
    post = db.relationship('Post', backref = 'author', lazy = True) # Connects which user actually creates the specific post

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = self.set_password(password) 

    def __repr__(self): 
        return '{} has been created'.format(self.username) # Lets us see what is being created  

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

class Fantasy(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    dropdown_list = db.Column(db.String(100))
    first_player = db.Column(db.String(300))
    second_player = db.Column(db.String(300))
    third_player = db.Column(db.String(300))
    fourth_player = db.Column(db.String(300))

class Post(db.Model):
     id = db.Column(db.Integer, primary_key = True) 
     title = db.Column(db.String(200))
     content = db.Column(db.String(1000))
     date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) # Because of the relationship based on the user model; we're saying we have a relationship with the Post Class and User Class showing us which post was made by which user. 
     # Relationship between user and post: user can make many posts but a post is associated with only user
     # USER_ID => 1
     # POST_ID: 23 => Created by USER_ID: 1  


    # Shows the reader what the title of the post is and which user posted it
     def __repr__(self):
        return "The Title is {} and the user is {}".format(self.title,self.user_id) # Printing something out to the console everytime a new post is created


