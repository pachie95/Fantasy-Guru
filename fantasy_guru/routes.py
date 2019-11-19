from fantasy_guru import app, db
from flask import render_template, request, flash, redirect, url_for

# Import of Forms -- Now have a form to our route 
from fantasy_guru.forms import RegisterForm, LoginForm, PostForm,FantasyForm

# Import Models
from fantasy_guru.models import User,Post,check_password_hash

# Flask-Login imports
from flask_login import login_required,current_user,login_user,logout_user

# Importing csv
import csv
import math
import numpy as np
import pandas as pd

def open_csv(filename, d=','):
    # define an empty list to store data
    data = []
    
    # use the 'with' keyword to load from csv and store into data
    with open(filename, encoding='utf-8') as mData:
        # use reader method in csv package to create python list
        info = csv.reader(mData, delimiter=d)
        # print(info)
        
        # loop over info and append to data
        for row in info:
            data.append(row)
        
    # no need to close file, using with statement closes automatically
    return data

csv_data = open_csv('files/Projections.csv')


# Route to take user to home after clicking title
@app.route("/") # a decorator
def home():
    posts = Post.query.all()
    return render_template("home.html", posts = posts)

@app.route("/help", methods=["GET","POST"])
def help():
    posts = Post.query.all()
    fantasy_form = FantasyForm()
    results1 = ""
    results2 = ""
    if request.method == 'POST':
        df = pd.read_csv('files/Projections.csv')
        week = int(dict(fantasy_form.dropdown_list.choices).get(fantasy_form.dropdown_list.data))
        first_player = fantasy_form.first_player.data
        second_player = fantasy_form.second_player.data
        results1 = df.loc[(df['Name'] == first_player) & (df['Week'] == int(week))][["Name","FantasyPointsYahoo"]].to_string().strip('Name FantasyPointsYahoo')
        print(results1)
        results2 = df.loc[(df['Name'] == second_player) & (df['Week'] == int(week))][["Name","FantasyPointsYahoo"]].to_string().strip('Name  FantasyPointsYahoo')
        # print(results2)
    return render_template('help.html', fantasy_form = fantasy_form, results1 = results1,results2 = results2)


# Route to take user to registration form
@app.route("/register", methods=["GET", "POST"])
def createUser():
    form = RegisterForm() # Instansiating a new form;
    if request.method == 'POST' and form.validate(): # If user requests a post request whatever
        flash("Thanks for signing up!")
        # Gathering Form Data
        username = form.username.data 
        email = form.email.data
        password = form.password.data
        print(username,email,password)

        # Add Form Data to User Model Class
        user = User(username, email, password)
        db.session.add(user) # Start communication with Database
        db.session.commit() # Save Data to Database
        return redirect(url_for('login'))
    else:
        flash("Your form is missing some data")
    return render_template("register.html", register_form=form)


# Route to take user to login form page
@app.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user_email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == user_email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username)
            return redirect(url_for('home'))
    else:
        print('Not Valid')
    return render_template('login.html',login_form=form)

# Route to let a user logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

# Route to let a user make a post/comment on potential fantasy players to discuss among other users    
@app.route('/post',methods=["GET", "POST"])
@login_required
def post():
    form = PostForm()
    title = form.title.data
    content = form.content.data
    user_id = current_user.id



    # Instatiate Post Class
    post = Post(title = title, content= content, user_id = user_id)
    db.session.add(post)
    db.session.commit()
    return render_template('post.html',post_form=form)

# Route to post what user posted
@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

