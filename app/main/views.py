from flask import render_template,request,redirect,url_for, abort, flash
from . import main
from sqlalchemy import asc
from ..models import  User,Notes
from flask_login import login_required, current_user
from .forms import NotesForm,UpdateProfileForm
from .. import db, bcrypt
from PIL import Image
import os, secrets


# Views
@main.route('/')
@login_required
def index():
    '''
    View root page function that returns the index page and its data
    '''
    notes = Notes.query.order_by(Notes.id.desc())
    return render_template('index.html', title ="Home",notes=notes)


"""NEW NOTES VIEW"""
@main.route('/notes/new', methods = ['GET','POST'])
@login_required
def new_note():
    form = NotesForm()
    if form.validate_on_submit():
        new_notes = Notes(title = form.title.data, notes=form.notes.data, user_id=current_user.id)
        db.session.add(new_notes)
        db.session.commit()
        flash("Notes save successfully!", "success")
        return redirect(url_for('main.index'))
    return render_template('create_note.html',legend="TAKE NOTES", title = "New Note", form=form)

"""individual NOTES"""
@main.route('/notes/<id>', methods = ['GET','POST'])
@login_required
def notes(id):
    notes = Notes.query.get_or_404(id) 
    return render_template('notes.html', title = "Notes", note=notes)

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
  

def save_picture(form_pic):
    random_hex=secrets.token_hex(8)
    _, f_ext=os.path.splitext(form_pic.filename)
    picture_fn = random_hex + f_ext 
    picture_path = os.path.join('app/static/images',picture_fn)
    # os.path.join('app/static/profile_images',picture_fn)
    form_pic.save(picture_path)
    output_size=(125,125)
    i = Image.open(form_pic)
    i.thumbnail(output_size)

    i.save(picture_path)
    return picture_fn

"""PROFILE NOTES VIEW"""
@main.route('/profile', methods = ['GET','POST'])
@login_required
def profile():
    '''
    Profile view to update profile
    '''   
    form=UpdateProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
                picture_file=save_picture(form.picture.data)
                current_user.image_file=picture_file

        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash("Your profile has been updated", "success")
        return redirect(url_for('main.profile'))

    form.username.data =current_user.username
    form.email.data =current_user.email
    return render_template('profile.html', title = "New Note", form=form)

