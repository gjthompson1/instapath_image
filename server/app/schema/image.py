from app import db

from .meta import Base

class Image(Base):
    __tablename__ = 'image'

    filepath = db.Column(db.String)
    username = db.Column(db.String)

    def __init__(self, filepath, username):
        self.filepath = filepath
        self.username = username

    def to_dict(self):
        d = {}
        d['id'] = self.id
        d['created_at'] = self.created_at
        d['filepath'] = self.filepath
        d['username'] = self.username
        return d
