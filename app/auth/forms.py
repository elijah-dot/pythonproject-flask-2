from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Email,EqualTo,DataRequired
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('enter your email address')
    author = StringField('Enter your name')
    password = StringField('Enter your password', validators=[DataRequired(),EqualTo('password_confirm',message='password must match')])
    password_confirm = PasswordField('Confirm passwords', validators=[DataRequired()])
    submit = StringField('Sing up')
    
    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('there is an account with that email')
        
    def validate_author(self,data_field):
        if User.query.filter_by(author=data_field.data).first():
            raise validationError('That author name is taken')
        
class LoginForm(FlaskForm):
    email = StringField('Your Email Address')
    password = PasswordField('Password',validators = [DataRequired(),Email()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')
    
