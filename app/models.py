from . import db
from werkzeug.security import generate_password_hash,check_password_hash





class Writer(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
     pass_secure = db.Column(db.String(60))
    # blogs = db.relationship('Blog')
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
        return f'User {self.username}'
    
    
    
        
    def save_writer(self):
        Writer.all_writers.append(self)
        
    @classmethod
    def get_writes(cls,id):
        return response  
    
    
# class Blog(db.Model):
#     '''
#     Blog class to define Blog Objects
#     '''

#     def __init__(self,id,title,content,date_posted):
#         self.id =id
#         self.title = title
#         self.content = content
#         self.date_posted = date_posted
        
        
#     def save_(self):
#         Blog.all_blog.append(self)
        
#     @classmethod
#     def get_blog(cls,id):
#         return response  
    
        
        