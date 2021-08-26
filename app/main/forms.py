from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired
from wtforms.validators import Required, ValidationError, Length, Email
from flask_login import current_user
from ..models import User

class NotesForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    notes = TextAreaField('Notes',validators=[DataRequired()])
    submit = SubmitField('Save Notes',validators=[DataRequired()])

class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    picture=FileField("Update Profile Picture", validators=[FileAllowed(['jpg','png','jpeg'])] )   
    submit = SubmitField('Update Profile')

    def validate_username(self, username):
        if username.data != current_user.username:
           user = User.query.filter_by(username=username.data).first()
           if user:
               raise ValidationError("Username Taken")
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email has already been registered")
                
class CreateNote(FlaskForm):
    title = StringField('Title',validators=[Required()])
    content = TextAreaField('Note content',validators=[Required()])
    category = SelectField('Category',choices=[('To do list','To do list'),('Items to remember','Items to remember'),('Online resources','Online resources')('General','General')],validators=[Required()])
    submit = SubmitField('Add')