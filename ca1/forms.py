from logging import PlaceHolder
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, SelectField, RadioField, IntegerField, DecimalField, FloatField, PasswordField, SelectMultipleField
from wtforms.validators import InputRequired, EqualTo

class ArtistForm(FlaskForm):
    
    answer= RadioField( choices=[ "Yes","No"])
    submit = SubmitField("Next:")

class RegistrationForm(FlaskForm):
    user_id=StringField("User id:", validators=[InputRequired()])
    password=PasswordField("Password:", validators=[InputRequired()])
    password2=PasswordField("Confirm Password:", 
        validators=[InputRequired(), EqualTo("password")])
    submit=SubmitField("Submit:")

class LoginForm(FlaskForm):
    user_id=StringField("User id:", validators=[InputRequired()])
    password=PasswordField("Password:", validators=[InputRequired()])
    submit=SubmitField("Submit:")

class MailForm(FlaskForm):
    name=StringField("Enter name:", validators=[InputRequired()])
    email=StringField("Enter email:", validators=[InputRequired()])
    submit = SubmitField("Submit:")

class AddArtistForm(FlaskForm):

    name=StringField("Name:", validators=[InputRequired()])
    rec=IntegerField("Rec Number:", validators=[InputRequired()])
    song=StringField("Song:", validators=[InputRequired()])
    link=StringField("Link to Spotify:", validators=[InputRequired()])
    submit=SubmitField("Submit:")

class RecommendationForm(FlaskForm):
    name=StringField("Name:", validators=[InputRequired()])
    rec=StringField("Write a recommendation here:", validators=[InputRequired()])
    submit=SubmitField("Submit:")