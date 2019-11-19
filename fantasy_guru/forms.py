from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from flask_wtf import FlaskForm


# Python Classes that represent our forms for people to register and login
# Will automatically be converted to html within our template



class FantasyForm(FlaskForm): 
    weeks = [('week10', '10'), ('week11', '11'), ('week12', '12'), ('week13', '13'), ('week14', '14'), ('week15', '15'), ('week16', '16'), ('week17', '17')]
    dropdown_list = SelectField('Select Week', choices = weeks)
    first_player = StringField('Content', validators=[DataRequired()])
    second_player = StringField('Content', validators=[DataRequired()])
    third_player = StringField('Content', validators=[DataRequired()])
    fourth_player = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('View Advice')

class RegisterForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired(),Email()])
    password = PasswordField("Password:", validators=[DataRequired()])
    confirm_pass = PasswordField("Confirm Password:", validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField() 

class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(),Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField()

class PostForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    content = StringField('Content:', validators=[DataRequired()])
    submit = SubmitField()    