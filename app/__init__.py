from flask import Flask
from config import  config_options
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app(config_name):
    app= Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])


    #initializing flask extensions
    #eg  bootstrap.inita_app(app)
    db.init_app(app)




    #register Blueprint
    from .main import main as main_Blueprint
    app.register_blueprint(main_Blueprint)



    return app