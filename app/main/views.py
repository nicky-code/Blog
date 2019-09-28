from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import Writer,Blog
from .forms import BlogForm,UpdateProfile
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
     
     
@main.route('/writer/<uname>')
def profile(uname):
    writer = Writer.query.filter_by(username = uname).first()

    if writer is None:
        abort(404)

    return render_template("profile/profile.html", writer = writer)


@main.route('/writer/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    writer = Writer.query.filter_by(username = uname).first()
    if writer is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        writer.bio = form.bio.data

        db.session.add(writer)
        db.session.commit()

        return redirect(url_for('.profile',uname=writer.username))

    return render_template('profile/update.html',form =form)
