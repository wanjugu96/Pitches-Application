from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment
from .. import db, photos
from .forms import UpdateProfile,submitpitchform,submitcommentform


@main.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        category=request.form['category']

        return redirect(url_for('.pitches',category=category))


    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    user_idd=user.id
    pitches=Pitch.query.filter_by(user_id=user_idd).all()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user,pitches=pitches)    


@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form=UpdateProfile()

    if form.validate_on_submit():
        user.bio=form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect (url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form=form)


@main.route('/user/<pitchid>/comments',methods=['GET','POST'])
@login_required
def comment(pitchid):
    pitch=Pitch.query.filter_by(id=pitchid).first()
    form=submitcommentform()
    if request.method =='POST' and form.validate_on_submit():
        comment=Comment(comment=form.comment.data,user_id=current_user.id,name=current_user.username,pitch_id=pitchid)
        db.session.add(comment)
        db.session.commit()

        pitchid=pitchid
        category=pitch.category
        

        return redirect (url_for('main.singlepitch',pitchid=pitchid,category=category))

    return render_template('pitch/comments.html',form=form,pitchid=pitchid)

@main.route('/<category>/<pitchid>')
def singlepitch(pitchid,category):
    comments=Comment.query.filter_by(pitch_id=pitchid).all()
    pitch=Pitch.query.filter_by(id=pitchid).first()
    category=pitch.category
    
    return render_template('pitch/singlepitch.html',category=category,pitch=pitch,comments=comments)


@main.route('/user/<uname>/update/pic' , methods=['POST','GET'])
@login_required
def update_pic(uname):
    user=User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])

        path=f'photos/{filename}'
        user.profilepicpath=path

        db.session.commit()
        return redirect(url_for('main.profile',uname=uname))


@main.route('/submitpitch',methods=['GET','POST'])
@login_required
def submitpitch():
    form=submitpitchform(request.form)

    id=current_user.id
    
    
    if request.method =='POST' and form.validate_on_submit():
        pitch=Pitch(title=form.title.data,pitch=form.pitch.data,user_id=id,category=form.category.data,name=current_user.username)
        db.session.add(pitch)
        db.session.commit()

        categoryy=form.category.data
        
        #return redirect(url_for('main.profile',uname=uname))
        
        return redirect(url_for('.pitches',category=categoryy,))
                
        #return redirect(url_for('.index'))category
    
    category=form.category.data

    #return redirect(url_for('.pitches',category=form.category.data))
    
    return render_template('pitch/submitpitch.html',form=form,name=current_user.username,user_id=id,category=category)
    


@main.route('/<category>',methods=['GET','POST'])   
def pitches(category):
    #allpitches=[]
    Allpitches=Pitch.query.filter_by(category=category).all()

    return render_template('pitch/pitches.html',category=category,Allpitches=Allpitches)


