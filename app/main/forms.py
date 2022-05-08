from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    title = StringField('Pitch Title')
    category = SelectField('Pitch Category')
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comment')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('What you aspire to be in life', validators=[DataRequired()])
    submit = SubmitField('Submit')