from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required

from werkzeug.urls import url_parse
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User
from app.extensions import login
from app.utils import flash_errors


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        flash('You are logged in.', 'success')
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
            return redirect(next_page)
        else:
            flash_errors(form)
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    else:
        flash_errors(form)
    return render_template('auth/register.html', title='Register', form=form)
