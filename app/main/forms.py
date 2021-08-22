from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[DataRequired()])
    review = TextAreaField('Movie review')
    # submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    picture = FileField("Update profile picture", validators=[FileAllowed(['png','jpg','jpeg'])])
    submit = SubmitField('Submit')
