from sqlalchemy.orm import relationship

from app.extensions import db

class Subject(db.Model):
    __tablename__ = "subject"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
