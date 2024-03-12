from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from app.extensions import db

class Thread(db.Model):
    __tablename__ = "thread"
    id = db.Column(db.Integer, primary_key=True ,autoincrement=True)
    theme_id = db.Column(db.Integer)
    title = db.Column(db.String(150))
    desc = db.Column(db.String(250))
    files = db.Column(db.String(500))


    def __repr__(self):
        return f'<Thread "{self.title}">'
