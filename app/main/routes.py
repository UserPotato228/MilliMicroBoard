from app.main import bp
from flask import render_template
from app.extensions import db
from app.models.subject import Subject
from app.models.theme import Theme

@bp.route('/')
def index():
    subjects = Subject.query.all()
    themes = Theme.query.all()
    return render_template("index.html", subjects=subjects, themes=themes)
