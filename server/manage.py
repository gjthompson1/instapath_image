# manage.py

import unittest

from flask_script import Manager
from flask_cors import CORS

from app import app, db
# from app.schema import User

manager = Manager(app)

@manager.command
def db_setup():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    manager.run()
