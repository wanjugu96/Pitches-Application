import os
from re import DEBUG 

class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:Serum2551@localhost/pitches'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST='app/static/photos'

    DEBUG=True
    TEMPLATES_AUTO_RELOAD = True

    #email configurations
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
    SIMPLE_JS_IIFE=True
    SIMPLEMDE_USE_CDN = True


class ProdCofig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://sahydrmkiripym:f92a1811d607730877fec6c5b6b2f378f886ad241f3fc0165e7afc0d22120a69@ec2-35-174-122-153.compute-1.amazonaws.com:5432/d4l77q9ibqqkp9'

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG=True
    TEMPLATES_AUTO_RELOAD = True



config_options={
    'development':DevConfig,
    'production':ProdCofig,
    'test':Config
}

