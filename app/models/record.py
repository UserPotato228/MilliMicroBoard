from app.extensions import db

class Record(db.Model):
    __tablename__ = "record"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    thread_id = db.Column(db.Integer)
    author = db.Column(db.String(50), default="Aноним")
    message = db.Column(db.String(350))
    replay = db.Column(db.Text)
    files = db.Column(db.Text)
