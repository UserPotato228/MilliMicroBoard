import os

from app.themes import bp
from flask import render_template, request, redirect
from app.extensions import db
from app.models.thread import Thread
from app.models.theme import Theme
import datetime
from config import Config

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@bp.route("/<string:tag>/", methods = ["GET", "POST"])
def theme(tag):
    if request.method == "GET":
        try:
            theme = db.session.query(Theme.id, Theme.title).filter_by(tag = tag).first()
            thread = db.session.query(Thread).filter_by(theme_id = theme[0]).all()
            return render_template("theme.html", title=theme[1], threads= thread)
        except:
            return render_template("notfound.html"), 404
    if request.method == "POST":
        print(request.method)
        theme_id = db.session.query(Theme.id).filter_by(tag = tag).first()[0]
        title = request.form.get("title", None)
        desc = request.form.get("desc", None)

        if not title:
            return redirect(request.url)
        file = request.files["file"]
        print("%s\n%s\n%s\n%s"%(theme_id, title, desc, file.filename))
        if file and allowed_file(file.filename):
            file.filename = "%s.%s"%(datetime.datetime.now().strftime("%Y%m%d%H%M%S"), file.filename.split(".")[len(file.filename.split("."))-1])
            file.save(os.path.join(Config.UPLOAD_FOLDER, file.filename))
        thread = Thread(theme_id = theme_id, title = title, desc = desc, files = file.filename)
        db.session.add(thread)
        db.session.commit()
        return redirect(request.url)
