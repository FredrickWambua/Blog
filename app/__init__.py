from flask import Flask, app
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads, IMAGES
from flask_migrate import Migrate, migrate


db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
migrate = Migrate()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos', IMAGES)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

   # registering the blueprint function
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    configure_uploads(app,photos)
    mail.init_app(app)
    migrate.init_app(app,db)

    return app