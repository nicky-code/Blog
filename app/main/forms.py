from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, PasswordField, ValidationError, BooleanField, SelectField,RadioField 
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
    
#Blog Form
class BlogForm(FlaskForm):
    title=StringField('Add your title blog')
    post = TextAreaField('Kindly post your Blog')  
    submit = SubmitField('Submit Blog')
    
    