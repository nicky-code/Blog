from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import Writer,Blog,Comment
from .forms import BlogForm,UpdateProfile,CommentForm
from .. import db,photos
# import requests
from ..requests import getQuotes

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    blog = Blog.query.all()
    comment=Comment.get_comments(id)
    quotes =getQuotes
    
    
    return render_template('index.html', current_user= current_user, blog= blog,quotes=quotes)


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
    blog = Blog.query.filter_by(writer_id=current_user.id).first()
    if writer is None:
        abort(404)

    return render_template("profile/profile.html", writer = writer,blog=blog)


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


@main.route('/writer/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    writer = Writer.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        writer.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/blog/update/<int:id>', methods = ['GET','POST'])
@login_required
def blog_update(id):
    form = BlogForm()
    blog = get_blog(id)
    if form.validate_on_submit():
        
        name = form.name.data
        

        # Updated review instance
        new_blog = Blog(id=blog.id,name=name)

        # save review method
        new_blog.save_blog()
        return redirect(url_for('.index',id = blog.id ))

    title = f'{blog.title} blogpost'
    return render_template('new_blog.html',title = title, blog_form=form, blog=blog)

@main.route('/new_comment/<int:id>', methods=['GET', 'POST'])
def new_comment(id):
    '''
    Function that adds a comment
    '''
    form = CommentForm()
    comment = Comment.query.filter_by(blog_id=id).first()
    blogs = Blog.query.filter_by(id=id).first()
    writer = Writer.query.filter_by(id=id).first()
    title =f'Welcome to blog Comments'
    
    if form.validate_on_submit():
        feedback = form.comment.data
        new_comment = Comment(feedback=feedback, writer_id=current_user.id, blog_id=blogs.id)
        new_comment.save_comment()
        
        return redirect(url_for('.index',uname=current_user.username))
    return render_template('comment.html',title=title, comment_form=form, blogs=blogs, comment=comment)


@main.route("/blog/<int:id>/delete", methods=['GET', 'POST'])
@login_required
def delete_post(id):
    blog=Blog.query.filter_by(id=id).first()
    
    if blog is None:
        abort(404)
        db session.delete(blog)
        db session.commit()
     
    return redirect(url_for('main.index'))


@main.route("/comment/<int:id>/delete", methods=['GET', 'POST'])
@login_required
def delete_comment(id):
    comment= Comment.query.filter_by(id=id).first()
    
    if comment is None:
        abort(404)
        db session.delete(comment)
        db session.commit()
     
    return redirect(url_for('main.index'))

    
        