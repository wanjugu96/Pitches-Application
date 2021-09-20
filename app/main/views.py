from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required


@main.route('/')
def index():
    return render_template('index.html')

# @main.route('/category/comments/new/<int:id>',methods=['GET','POST'])
# def comment():
#     @login_required
#     pass