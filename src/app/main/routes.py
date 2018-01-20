from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app.main import main
from app.main.forms import EditProfileForm, PostForm
from app.models import User, Post


@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    post_form = PostForm()
    if post_form.validate_on_submit():
        Post.create(body=post_form.post.data,
                    author=current_user)
        flash('Your post is now live!')
        return redirect(url_for('main.index'))
    posts = current_user.followed_posts()
    return render_template('index.html',
                           title='Home',
                           form=post_form,
                           posts=posts)

@main.route('/explore')
@login_required
def explore():
    posts = Post.query.order_by(Post.timestamp.desc())
    return render_template('index.html', 
                           title='Explore', 
                           posts=posts)


@main.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)

# @user.route('/profile', methods=['GET', 'POST'])
# @login_required
# def profile():
#     form = ProfileForm(obj=current_user)
#     if form.validate_on_submit():
#         form.populate_obj(current_user)
#         current_user.update_at = get_current_time()
#         db.session.commit()
#         flash('Public profile updated.', 'success')
#     return render_template('user/profile.html', form=form)
