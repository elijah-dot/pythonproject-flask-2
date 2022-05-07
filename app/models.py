from . import db, login_manager
from flask_login import UserMixin ,current_user
from  werkzeug.security import generate_password_hash,check_password_hash

#model class for user
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),unique=True,nullable=False)
    email = db.Column(db.String(255),unique=True,nullable=False)
    secure_password = db.Column(db.String(255),nullable=False)
    bio = db.Column(db.string(255))
    profile = db.Column(db.String())
    # user oriented
    pitches = db.relationship('Pitch', backref= 'user',lazy= 'dynamic')
    comment = db.relationship('Comment', backref= 'user',lazy= 'dynamic')
    upvote = db.relationship('Upvote', backref= 'user',lazy= 'dynamic')
    downvote= db.relationship('Downvote', backref= 'user',lazy= 'dynamic')
    # commit and save
    
    @property
    def set_password(self):
        raise AttributeError('you cannot read the password')
    
    @set_password.setter
    def password(self,password):
        self.secure_password = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self,secure_password,password)
    
    def save_u(self):
        db.session.add()
        db.session.commit()
        
    def __repr__(self):
        return f'User {self.username}'

    

#model class for category
#model class for pitches
#model class for votes
#model class for comments