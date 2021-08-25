from flask import render_template,request,redirect,url_for, abort, flash
from . import main
from sqlalchemy import asc
from ..models import  User,Notes
from flask_login import login_required, current_user
from .forms import NotesForm,UpdateProfileForm
from .. import db
from PIL import Image
import os, secrets


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html', title ="Home")


"""NEW NOTES VIEW"""
@main.route('/notes/new', methods = ['GET','POST'])
# @login_required
def new_note():
    form = NotesForm()
    return render_template('create_note.html', title = "New Note", form=form)


"""PROFILE NOTES VIEW"""
@main.route('/profile/<username>', methods = ['GET','POST'])
# @login_required
def profile(username):
    '''
    Profile view to update profile
    '''   
    form=UpdateProfileForm()
    return render_template('profile.html', title = "New Note", form=form)

