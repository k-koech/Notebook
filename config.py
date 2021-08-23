import os 


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = '<Flask WTF Secret Key>'
    
    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com' 
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "triplek901@gmail.com"
    MAIL_PASSWORD ="kelvin97"   
    MAIL_DEBUG = True
    MAIL_SUPPRESS_SEND = False
    TESTING = False
    """ SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:kkkk@localhost/flaskmovie'
 """

class TestConfig(Config):
    pass 

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:kkkk@localhost/flaskmovie'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}