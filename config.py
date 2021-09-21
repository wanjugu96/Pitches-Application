import os
from re import DEBUG 

class Config:
    #sqlalchemy uri
    pass

class ProdCofig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:Serum2551@localhost/pitches'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST='app/static/photos'

    DEBUG=True
    TEMPLATES_AUTO_RELOAD = True

    #email configurations
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=25
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")


class TestConfig(Config):
    DEBUG=True
    TEMPLATES_AUTO_RELOAD = True



config_options={
    'development':DevConfig,
    'production':ProdCofig,
    'test':Config
}

