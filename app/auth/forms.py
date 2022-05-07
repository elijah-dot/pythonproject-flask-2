from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField,BooleanField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User

