from . import db, login_manager
from datetime import datetime
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
    
#model class for pitches
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.integer, primary_key=True)
    title = db.Column(db.string(255), nullable=False)
    post = db.Column(db.Text(),nullable=False)
    # user oriented
    comment = db.relationship('Comment', backref= 'user',lazy= 'dynamic')
    upvote = db.relationship('Upvote', backref= 'user',lazy= 'dynamic')
    downvote= db.relationship('Downvote', backref= 'user',lazy= 'dynamic')
    
    user_id = db.Column(db.integer,db.ForeignKey('users.id'))
    time = db.Column(db.Datetime,default=datetime.utcnow)
    category = db.Column(db.String(255),index=True,nullable=False)
    
    def save_p(self):
        db.session.add(self)
        db.session.commit()
        
    def __repr__(self):
        return f'Pitch {self.post}'
    
    
#model class for comments
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.Text(),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)
    
    def save_c(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()
        
        return comments
    
    
    def __repr__(self):
        return f'comment:{self.comment}'
    
    #model class for upvotes
    
class Upvote(db,Model):
    __tablename__='upvote'
    
    id = db.Column(db.integer, primary_key=True)
    user_id = db.Column(db.integer,db.ForeignKey('users.id'))
    pitch_id= db.Column(db.integer, db.ForeignKey('pitches.id'))
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote
    
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
    
         
        #model class for downvotes
class Downvote(db,Model):
    __tablename__ = 'downvotes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    


