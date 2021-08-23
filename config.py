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

class TestConfig(Config):
    pass 
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://durnhuwzllfwpb:c1e2d92e044252629d20c8bfe86d28894fd13079b877ca3ac0700371387595bd@ec2-54-196-65-186.compute-1.amazonaws.com:5432/dbluoqucc3nuvv'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}