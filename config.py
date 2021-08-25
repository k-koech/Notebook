import os 


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'jihesgvuys'
 

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