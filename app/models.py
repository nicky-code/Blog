






class Writer:
    '''
    Writer class to define Writer Objects
    '''

    def __init__(self,id,username,email,password):
        self.id =id
        self.username = username
        self.email = email
        self.password = password

        
    def save_writer(self):
        Writer.all_writers.append(self)
        
    @classmethod
    def get_writes(cls,id):
        return response  
    
    
class BlogPost:
    '''
    BlogPost class to define BlogPost Objects
    '''

    def __init__(self,id,title,content,date_posted):
        self.id =id
        self.title = title
        self.content = content
        self.date_posted = date_posted
        
        
    def save_(self):
        BlogPost.all_blogPost.append(self)
        
    @classmethod
    def get_blogPost(cls,id):
        return response  
    
        
        