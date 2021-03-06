from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import User
from application import db


user_signup = Blueprint('user_signup', __name__, template_folder='templates')

@user_signup.route('/usersignup')
def show_user_signup():
    return render_template('user_signup.html', current_page='user_signup')

@user_signup.route('/usersignup', methods=['GET', 'POST'])
def show_user_signup_post():
    email = request.form.get('email')
    username = request.form.get('username')
    name = request.form.get('name')
    password = request.form.get('password')
    confirm_password = request.form.get('confirmpassword')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('user_signup.show_user_signup'))

    if password == confirm_password:
        new_user = User(email=email, username=username, name=name, password=generate_password_hash(password, method='sha256'))
    else:
        flash('Passwords do not match! Please try again!')
        return redirect(url_for('user_signup.show_user_signup'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('user_login.show_user_login'))
