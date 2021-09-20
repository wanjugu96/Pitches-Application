from app.auth.forms import RegistrationForm
from flask import render_template,redirect,url_for
from . import auth 
from .forms import RegistrationForm
from .. import db
from ..models import User



@auth.route('/register',methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)







@auth.route('/login')
def login():
    return render_template('login.html')
