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

"""DELETE NOTES"""
@main.route('/notes/delete/<id>', methods = ['POST'])
@login_required
def delete_notes(id):
    notes = Notes.query.get_or_404(id)
    db.session.delete(notes)
    db.session.commit()
    flash("Notes deleted", "success")
    return redirect(url_for("main.index"))
"""UPDATE NOTES"""
@main.route('/notes/update/<id>', methods = ['GET','POST'])
@login_required
def update_notes(id):
    notes = Notes.query.get_or_404(id)
    form = NotesForm()
    if form.validate_on_submit():
        notes.title = form.title.data
        notes.notes = form.notes.data
        db.session.commit()
        flash("Changes saved successfully", "success")
        return redirect(url_for('main.notes', id=notes.id))
    elif request.method == "GET":
        form.title.data = notes.title
        form.notes.data = notes.notes
        title = "Update Post"
        return render_template("create_note.html", title=title, legend="Update Notes",form=form,)
