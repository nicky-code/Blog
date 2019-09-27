from flask import render_template
from . import main
from flask_login import login_required
from ..models import Writer,Blog
from .forms import  BlogForm
from .. import db


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    blogs = Blog.query.all()
    
    
    print(blogs)

    
    return render_template('index.html', blogs= blogs)


@main.route('/add/blog/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_blog():
    '''
    View new route function that returns a page with a form to create a blog
    '''

    form = BlogForm()
    
    if form.validate_on_submit():
        name = form.name.data
        new_blog= Blog(name=name)
        new_blog.save_category()
        
        return redirect(url_for('.index'))
    
    title = 'New blog'
    return render_template('new_blog.html', blog_form = form, title = title)
     