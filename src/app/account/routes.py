from flask import (
    render_template, 
    flash, 
    redirect, 
    url_for, 
    request
)
from flask_login import (
    login_user, 
    logout_user,
    current_user,
    login_required
)

from werkzeug.urls import url_parse
from app.account import account
from app.account.forms import LoginForm, RegistrationForm
from app.models import User
from app.extensions import login
from app.utils import flash_errors


@account.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    login_form = LoginForm(request.form)
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        remember_me = login_form.remember_me.data
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('account.login'))
        login_user(user, remember=remember_me)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('account/login.html', title='Sign In', form=login_form)

@account.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@account.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    registration_form = RegistrationForm(request.form)
    if registration_form.validate_on_submit():
        User.create(username=registration_form.username.data,
                    email=registration_form.email.data,
                    password=registration_form.password.data)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('account.login'))
    return render_template('account/register.html', title='Register',
                           form=registration_form)
