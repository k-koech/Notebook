import os 


class Config:
    '''
    General configuration parent class
    '''
    MOVIES_API_KEY = '191743892af9cad7b309cd56ee66ad46'
    SECRET_KEY = '<Flask WTF Secret Key>'
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    SECRET_KEY = '<Flask WTF Secret Key>'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com' 
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "triplek901@gmail.com"
    MAIL_PASSWORD ="kelvin97"

    

     # simple mde  configurations
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:kkkk@localhost/flaskmovie'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:kkkk@localhost/flaskmovie'
 
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kkkk@localhost/flaskmovie'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}