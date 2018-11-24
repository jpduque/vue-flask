import os
from flask import Flask, current_app, send_file
from .api import api_bp
from .client import client_bp

app = Flask(__name__)

app.register_blueprint(api_bp)
app.register_blueprint(client_bp)

from .config import Config

app.logger.info('>>> {}'.format(Config.FLASK_ENV))

@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    app.config['STATIC_FOLDER'] = os.path.join(dist_dir, 'static')
    app._static_folder = os.path.join(dist_dir, 'static')
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)
