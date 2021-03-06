#from app.auth.views import login
from flask import Flask
from config import  config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE
#from app.models import User
# from app import login

simple =SimpleMDE()
bootstrap=Bootstrap()
db=SQLAlchemy()
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

photos=UploadSet('photos',IMAGES)

#configure UploadSet


mail = Mail()


def create_app(config_name):
    app= Flask(__name__)

    mail.init_app(app)

    simple.init_app(app)
    #creating app configurations
    app.config.from_object(config_options[config_name])

    configure_uploads(app,photos)


    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    login_manager.init_app(app)

    # @login.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))


    #register Blueprint
    from .main import main as main_Blueprint
    app.register_blueprint(main_Blueprint)

    from .auth import auth as auth_Blueprint
    app.register_blueprint(auth_Blueprint,url_prefix='/authenticate')



    return app