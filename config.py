import os
basedir = os.path.abspath(os.path.dirname(__file__)) # Tells python to look at all files the same on ANY operating system
# Windows: \ 
# Mac & Linux: / 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Telling SQLALCHEMY to NOT tell us things we already know