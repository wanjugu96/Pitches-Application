from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required,Email,EqualTo, ValidationError
 
class UpdateProfile(FlaskForm):
    bio=TextAreaField('Tes',validators=[Required()])
    submit=SubmitField('Submit')

class submitpitchform(FlaskForm):
    title=StringField('Title of your pitch',validators=[Required()])
    pitch=TextAreaField('Your pitch',validators=[Required()])
    
    category = SelectField('pitch category', choices = [('Business', 'Business'), 
      ('Sales', 'Sales'),('Job Interview','Job Interview'),('Pickup Lines','Pickup Lines')])

    submit=SubmitField('Submit')

class submitcommentform(FlaskForm):
    
    comment=TextAreaField('Your comment',validators=[Required()])
    
    submit=SubmitField('Submit')



