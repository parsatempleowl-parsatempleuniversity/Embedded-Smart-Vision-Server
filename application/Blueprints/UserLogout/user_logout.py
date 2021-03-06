from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import login_user, logout_user, login_required
from application import db
from application.models import User



user_logout = Blueprint('user_logout', __name__, template_folder="templates")



@user_logout.route('/userlogout')
@login_required
def show_user_logout():
	return render_template('user_logout.html', current_page='user_logout')

@user_logout.route('/userlogout', methods=['GET', 'POST'])
@login_required
def show_user_logout_post():
	email = request.form.get('email')
	user = User.query.filter_by(email=email).first()
	# user.is_authenticated = False
	# db.session.commit()
	return redirect(url_for('user_login.show_user_login'))
