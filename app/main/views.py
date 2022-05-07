from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required,current_user
from ..models  import User ,Pitch,Comment ,Upvote,Downvote
from .form import UpdateProfile,PitchForm,CommentForm
from .. import db,photos

@main.route('/')
def index():
    pitches = Pitch.query.all()
    job = Pitch.query.filter_by(category='Job').all()
    event =Pitch.query.filter_by(category = 'Events').all()
    advertisement = Pitch.query.filter_by(category = 'Advertisement').all()
    life = Pitch.query.filter_by(category = 'Life').all()
    return render_template('index.html', job = job,event = event, pitches = pitches,advertisement= advertisement,life = life)

@main.route('/create_new',methods= ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object  = Pitch(post = post, category = category, user_id = current_user.get_current_object().id,title=title,)
        new_pitch_object.save_p()
        return redirect(url_for('main.index'))
