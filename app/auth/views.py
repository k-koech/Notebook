from flask import render_template,redirect,url_for, flash,request
from . import auth
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db, bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user

@auth.route('/login',methods = ["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for("main.index"))
        else:
            flash(f"Invalid credentials", "danger")
    return render_template("auth/login.html", title="Login", form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f"Logout success!", "success")
    return redirect(url_for("auth.login"))