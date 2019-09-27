from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin




class Writer(UserMixin,db.Model):
    __tablename__ = 'writers'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
     pass_secure = db.Column(db.String(60))
    blogs = db.relationship('Blog')
    # comments = db.relationship('Comment')
    
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
        
    
    def __repr__(self):
        return f'Writer {self.username}'
    
    
    
        
    def save_writer(self):
        Writer.all_writers.append(self)
        
    @classmethod
    def get_writes(cls,id):
        return response  
    
    
class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    post = db.Column(db.String(255))
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    # comments = db.relationship('Comment')

    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def clear_blogs(cls):
        Blog.all_blogs.clear()
        
    
    def get_blogs(id):
        blogs = Blog.query.filter_by(writer_id=id).all()
        return blogs
    
    @classmethod
    def count_blogs(cls,uname):
        writer = Writer.query.filter_by(username=uname).first()
        blogs = Blog.query.filter_by(writer_id=writer.id).all()
        
        blogs_count = 0
        for blog in blogs:
            blogs_count += 1
            
        return blogs_count    
    
    
        
        