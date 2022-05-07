from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import login_required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title')
    category = SelectField('Pitch Category')
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comment')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('What you aspire to be in life', validators=[Required()])
    submit = SubmitField('Submit')