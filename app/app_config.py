import os

basedir = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(basedir, 'db')


class Config:
    APP_NAME = os.environ.get('APP_NAME') or 'APP'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    AUTH_USERNAME = os.environ.get('AUTH_USERNAME')
    AUTH_PASSWORD = os.environ.get('AUTH_PASSWORD')
    if not AUTH_USERNAME or not AUTH_PASSWORD:
        raise Exception('Auth credentials not set')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(DB_DIR, 'data-dev.sqlite')

    @classmethod
    def init_app(cls, app):
        pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(DB_DIR, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False

    @classmethod
    def init_app(cls, app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(DB_DIR, 'data.sqlite')
    SSL_DISABLE = (os.environ.get('SSL_DISABLE') or 'True') == 'True'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        assert os.environ.get('SECRET_KEY'), 'SECRET_KEY IS NOT SET!'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}