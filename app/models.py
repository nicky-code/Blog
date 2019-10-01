from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(writer_id):
    return Writer.query.get(int(writer_id))



class Writer(UserMixin,db.Model):
    __tablename__ = 'writers'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    blogger = db.relationship('Blog', backref='blogger', lazy='dynamic')
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    comments = db.relationship('Comment')
    blog = db.relationship('Blog', backref='writer', lazy='dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
        
    def save_writer(self):
        Writer.all_writers.append(self)
        
    @classmethod
    def clear_writers(cls):
        Writer.all_writers.clear()
        
    
    def __repr__(self):
        return f'Writer {self.username}'    
    
    
class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    post = db.Column(db.String(255))
    postedAt =  db.Column(db.DateTime,default=datetime.utcnow)
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    comments = db.relationship('Comment')
    feedback = db.Column(db.String(255))

    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def clear_blogs(cls):
        Blog.all_blogs.clear()
        
    
    def get_blogs(cls):
        blogs = Blog.query.filter_by(writer_id=id).all()
        return blogs
    
    def get_blog(id):
        blogs = Blog.query.filter_by(writer_id=id).all()
        return blogs
        
        
    
    
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    feedback = db.Column(db.String)
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(self,id):
        comment = Comment.query.filter_by().all()
        return comment       
        
        
        
class Quote :
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self,id,author,quote):
        self.id =id
        self.author= author
        self.quote = quote
        