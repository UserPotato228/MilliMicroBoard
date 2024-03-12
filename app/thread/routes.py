import os
import datetime

import config
from app.models.record import Record
from app.thread import bp
from app.extensions import db
from app.models.thread import Thread
from flask import render_template, request, flash, redirect

from config import Config

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@bp.route("/<string:tag>/<int:id>", methods=["GET", "POST"])
def thread(tag, id):
    if request.method == "GET":
        thread_info = db.session.query(Thread.title, Thread.desc, Thread.files).filter_by(id=id).first()
        records = db.session.query(Record).filter_by(thread_id = id).all() or None
        return render_template("thread.html", title = thread_info[0], desc = thread_info[1], file=thread_info[2], records=records)
    else:
        author = request.form.get("author") or "Анон"
        message = request.form.get("message", None)
        if not message:
            flash("Вы ничего не написали")
            return redirect(request.url)
        replay = request.form.get("replay", "")
        file = request.files["file"]
        print("%s\n%s\n%s\n%s"%(author, message, replay, file.filename))
        if file and allowed_file(file.filename):
            file.filename = "%s.%s"%(datetime.datetime.now().strftime("%Y%m%d%H%M%S"), file.filename.split(".")[1])
            file.save(os.path.join(Config.UPLOAD_FOLDER, file.filename))
        record = Record(thread_id = id, author = author, message = message, replay = replay, files = file.filename)
        db.session.add(record)
        db.session.commit()
        file = open(os.path.join(config.base_dir, "log.txt"), "a")
        file.write("%s; %s; %s;\n"%(request.remote_addr, id, message))
        return redirect(request.url)
