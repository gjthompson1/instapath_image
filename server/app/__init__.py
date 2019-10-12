# app/__init__.py

import os

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__, static_url_path='/static')

# enable CORS
CORS(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

db = SQLAlchemy(app)

# register blueprints
from app.api.ping import ping_blueprint
from app.api.images import images_blueprint

app.register_blueprint(ping_blueprint)
app.register_blueprint(images_blueprint)
