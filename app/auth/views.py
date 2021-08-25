from flask import render_template,redirect,url_for, flash,request
from . import auth
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash



@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    return render_template('auth/register.html',title="Login", form = form)

@auth.route('/login',methods = ["GET","POST"])
def login():
    login_form = LoginForm()
   
    title = "NoteBook login"
    return render_template('auth/login.html',form = login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))

