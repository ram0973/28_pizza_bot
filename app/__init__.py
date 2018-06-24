import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from app.app_config import config
from .main.views import main as main_blueprint

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    db.init_app(app)
    csrf.init_app(app)

    app.add_url_rule('/favicon.ico', 'favicon',
                     lambda: app.send_static_file('favicon.ico'))

    app.register_blueprint(main_blueprint)

    return app
