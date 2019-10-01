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
    quotes =getQuotes()
    
    
    return render_template('index.html',current_user=current_user,blog= blog, comment=comment, quotes=quotes)


@main.route('/add/blog/', methods = ['GET','POST'])
@login_required
def new_blog():
    '''
    View new route function that returns a page with a form to create a blog
    '''
    blog=Blog.query.filter_by(id=current_user.id).first()
    writer = Writer.query.filter_by(id = current_user.id).first()
    form = BlogForm()
    
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        
        new_blog= Blog(post=post,title=title)
        new_blog.save_blog()
        
        return redirect(url_for('.index'))
    
    title = 'New blog'
    return render_template('new_blog.html', blog_form = form,current_user=current_user)
     
     
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
    
    
    blog=Blog.query.filter_by(id=id).first()
    if blog is None:
        abort(404)
    form=BlogForm()
    if form.validate_on_submit():
        blog.title=form.title.data
        blog.post=form.post.data
        
       

        db.session.commit()
        
        return redirect(url_for('.index',blog_id=blog.id))
    else:
        form.title.data = blog.title
        form.post.data= blog.post
        
      
    return render_template('new_blog.html',blog_form=form, blog=blog)

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
        
        return redirect(url_for('.index'))
    return render_template('comment.html',title=title, comment_form=form, blogs=blogs, comment=comment)


@main.route("/index/<int:id>/delete_post", methods=['GET', 'POST'])
@login_required
def delete_post(id):
    
    current_blog=Blog.query.filter_by(id=id).first()
    writer = Writer.query.filter_by(id=id).first()
    
    if current_blog is None:
        abort(404)
    db.session.delete(current_blog)
    db.session.commit()
     
    return redirect(url_for('.index'))


@main.route("/index/<int:id>/delete_comment", methods=['GET', 'POST'])
@login_required
def delete_comment(id):
    current_blog= Comment.query.filter_by(id=id).first()
    print(current_user.id)
    print(current_blog.writer_id)
    
    if current_blog.writer_id != current_user.id:
        abort(404)
    else:
        db.session.delete(current_blog)
        db.session.commit()
     
        return redirect(url_for('.index'))

    # return render_template('comment.html', current_blog=current_blog)

    
        