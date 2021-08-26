import os
class Config:
    '''
    This is the general configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:12345@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST='app/static/photos'
    SECRET_KEY='987654321!'


    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'wambuafred13@gmail.com'




class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}