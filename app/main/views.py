from flask import render_template,request,redirect,url_for, abort
from . import main
from ..models import  Pitch, User, Upvote, Downvote
from flask_login import login_required, current_user
from .forms import ReviewForm,UpdateProfile
from .. import db, photos
import markdown2



# Views
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''


    title = 'Home - Welcome to The best Movie Review Website Online'
  
    pitches= Pitch.query.all()
    return render_template('index.html', title = title, pitches=pitches)

# @main.route('/search/<movie_name>')
# def search(movie_name):
#     '''
#     View function to display the search results
#     '''
#     movie_name_list = movie_name.split(" ")
#     movie_name_format = "+".join(movie_name_list)
#     searched_movies = search_movie(movie_name_format)
#     title = f'search results for {movie_name}'
#     return render_template('search.html',movies = searched_movies)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def pitch():
    if request.method=="POST":
        category = request.form['category']
        pitch = request.form['pitch']
        new_pitch = Pitch(category=category, pitch=pitch, user_id=current_user.id )
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index' ))
    else:
        return redirect(url_for('main.index' ))


@main.route('/upvote/<id>', methods = ['GET','POST'])
@login_required
def upvote(id):
    '''
    View movie page function that returns the movie details page and its data
    '''   
    if request.method=="POST":
        get_upvotes = Upvote.query.filter_by(pitch_id=id).first_or_404()
        votes = int(get_upvotes.votes)+2
        print(get_upvotes)

        pitch_id = id
        newUpvote = Upvote.query.filter_by(pitch_id=id).update({"votes": votes})

        newUpvote = Upvote(pitch_id = pitch_id, votes=10, user_id=current_user.id)
        db.session.add(newUpvote)
        db.session.commit()
        return redirect(url_for('main.index' ))

    return redirect(url_for('main.index' ))


# @main.route('/review/<int:id>')
# def single_review(id):
#     review=Review.query.get(id)
#     if review is None:
#         abort(404)
#     format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
#     return render_template('review.html',review = review,format_review=format_review)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))