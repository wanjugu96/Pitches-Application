from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required,Email,EqualTo, ValidationError
 
class UpdateProfile(FlaskForm):
    bio=TextAreaField('Tell us about you',validators=[Required()])
    submit=SubmitField('Submit')
