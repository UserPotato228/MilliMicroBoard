from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.extensions import db


class Theme(db.Model):
    __tablename__ = "theme"
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    subject_id = db.Column(db.Integer)
    tag = db.Column(db.String(5))
    title = db.Column(db.String(100))

    def __repr__(self):
        return f'<Theme "{self.tag}">'
