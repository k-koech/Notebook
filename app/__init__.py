from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_uploads import UploadSet,configure_uploads,IMAGES,patch_request_class

from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    db.init_app(app)
    login_manager.init_app(app)


    app.config.update(
    MAIL_USE_SSL = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USERNAME = "kalambanidouglas@gmail.com",
    MAIL_PASSWORD ="kalambani97?")
    
    mail.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
   

    # Initializing flask extensions
    bootstrap.init_app(app)

    # authenticating
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # Will add the views and forms
     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

