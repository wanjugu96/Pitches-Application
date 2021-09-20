from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from models import User


@main.route('/')
def index():
    return render_template('index.html')

def profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profile.html',user=user)    

@main.route('/comments',methods=['GET','POST'])
@login_required
def comment():
    return render_template('comments.html')

