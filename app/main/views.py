from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/comments',methods=['GET','POST'])
@login_required
def comment():
    return render_template('comments.html')

