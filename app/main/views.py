from flask import render_template,request,redirect,url_for, abort, flash
from . import main
from sqlalchemy import asc
from ..models import  Feedback, Pitch, User, Comments
from flask_login import login_required, current_user
from .forms import UpdateProfile
from .. import db
from PIL import Image
import os, secrets


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to One Minute Pitches'
    pitches= Pitch.query.order_by(Pitch.id.asc())
    pickup_pitches= Pitch.query.filter_by(category="Pickup lines").all()
    interview_pitches= Pitch.query.filter_by(category="Interview pitch").all()
    product_pitches= Pitch.query.filter_by(category="Product pitch").all()
    promotion_pitches= Pitch.query.filter_by(category="Promotion pitch").all()
    
    comments = Comments.query.all()
    print(pitches)
    return render_template('index.html', title = title, pitches=pitches, comments=comments,pickup_pitches=pickup_pitches,interview_pitches=interview_pitches,
    product_pitches=product_pitches,promotion_pitches=promotion_pitches )


@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def pitch():
    if request.method=="POST":
        category = request.form['category']
        pitch = request.form['pitch']
        new_pitch = Pitch(category=category, pitch=pitch, user_id=current_user.id )
        db.session.add(new_pitch)
        db.session.commit()
        flash('Saved successful')
        return redirect(url_for('main.index' ))
    else:
        return redirect(url_for('main.index' ))


@main.route('/comment/<id>', methods = ['GET','POST'])
@login_required
def comment(id):
    '''
    comments view that inserts comments to the database
    '''   
    if request.method=="POST":
        comment = request.form['comment']
        new_comment = Comments(pitch_id=id, comment=comment, user_id=current_user.id )
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment saved')
        return redirect(url_for('main.index' ))
    return redirect(url_for('main.index' ))


@main.route('/feedback', methods = ['GET','POST'])
@login_required
def feedback():
    '''
    A function to save feedbacks to the database
    '''   
    if request.method=="POST":
        feedback = request.form['feedback']
        new_feedback = Feedback(feedback=feedback, user_id=current_user.id )
        db.session.add(new_feedback)
        db.session.commit()
        flash('Your feedback has been received! Thank you!')
        return redirect(url_for('main.index' ))
    return redirect(url_for('main.index' ))


@main.route('/upvote/<id>', methods = ['GET','POST'])
@login_required
def upvote(id):
    '''
    View movie page function that returns the movie details page and its data
    '''   
    if request.method=="POST":
        get_upvotes = Pitch.query.filter_by(id=id).first_or_404()
        votes = get_upvotes.upvotes+1
        print(get_upvotes)

        newUpvote = Pitch.query.filter_by(id=id).update({"upvotes": votes})
        db.session.commit()
        return redirect(url_for('main.index' ))

    return redirect(url_for('main.index' ))


@main.route('/downvote/<id>', methods = ['GET','POST'])
@login_required
def downvote(id):
    '''
    Downvote function that saves the downvotes
    '''   
    if request.method=="POST":
        get_downvotes = Pitch.query.filter_by(id=id).first_or_404()
        votes = get_downvotes.downvotes-1

        newUpvote = Pitch.query.filter_by(id=id).update({"downvotes": votes})
        db.session.commit()
        return redirect(url_for('main.index' ))

    return redirect(url_for('main.index' ))


@main.route('/user/<uname>')
@login_required
def profile(uname):
    title = uname
    form = UpdateProfile()
    pitches= Pitch.query.order_by(Pitch.id.asc())
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user, title=title, form=form, pitches=pitches)



def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _, f_ext=os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = ""
    # os.path.join(root_path,'static/profile_images',picture_fn)
    
    output_size=(125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)
    return picture_fn
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        if form.picture.data:
            pic_file = save_picture(form.picture.data)
            user.image_file = pic_file
            user.bio = form.bio.data
            db.session.add(user)
            db.session.commit()
        flash('Profile Updated successfully!')
        return redirect(url_for('.profile',uname=user.username))

    if request.get == "GET":
        form.data.bio = current_user.bio
        return render_template('profile/update.html',form =form)



@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        # filename = photos.save(request.files['photo'])
        # path = f'photos/{filename}'
        # user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


