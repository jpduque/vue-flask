"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """

import os
from app import app


class Config(object):
    # If not set fall back to production for safety
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    # FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    # DIST_DIR = os.path.join(ROOT_DIR, 'frontend', 'dist')

    DIST_DIR = os.path.join(os.path.abspath(os.path.join(ROOT_DIR, os.pardir)), 'frontend', 'dist')

    if not os.path.exists(DIST_DIR):
        raise Exception(
            'DIST_DIR not found: {}'.format(DIST_DIR))


app.config.from_object('app.config.Config')
