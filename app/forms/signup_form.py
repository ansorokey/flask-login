from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
# We have been using DataRequired up until now
# Note that the documentation recommends using InputRequired

# All form classes should inherit from FlaskForm for additional properties and functions
class SignupForm(FlaskForm):
  first_name = StringField('First Name', validators=[DataRequired()])
  last_name = StringField('Last Name', validators=[DataRequired()])
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Log In')

  # A function to querythe database and find out if the username is unique
  # def validate_username(self, check_this):
  #   db_username = User.query.filter(User.username == check_this).first()
  #   if db_username is not None:
  #     raise ValidationError('Username is taken. Please choose another.')
