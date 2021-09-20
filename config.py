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

    DEBUG=True
    TEMPLATES_AUTO_RELOAD = True

class TestConfig(Config):
    DEBUG=True
    TEMPLATES_AUTO_RELOAD = True



config_options={
    'development':DevConfig,
    'production':ProdCofig,
    'test':Config
}

