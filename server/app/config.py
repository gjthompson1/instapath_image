# app/config.py

import os

class BaseConfig:
    """Base configuration"""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    UPLOAD_FOLDER = 'app/static/images'
    VIEW_FOLDER = 'static/images'