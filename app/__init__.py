from flask import Flask, send_from_directory, request, abort, render_template

import config
from config import Config
from app.extensions import db
from app.models.theme import Theme
from app.models.thread import Thread
import os

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #database
    db.init_app(app)
    print(db)

    # Blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.themes import bp as themes_bp
    app.register_blueprint(themes_bp)
    from app.thread import bp as thread_bp
    app.register_blueprint(thread_bp)

    @app.errorhandler(413)
    def request_entity_too_large(error):
        return render_template("limit.html"), 413

    @app.errorhandler(404)
    def request_not_found(error):
        return render_template("notfound.html"), 404

    @app.before_request
    def blacklist_():
        ip = request.remote_addr
        blacklist_file = open(os.path.join(config.base_dir,"blacklist.txt"), "r")
        blacklist = blacklist_file.read().splitlines()
        blacklist_file.close()
        if ip in blacklist:
            abort(403)
        print("%s good addr"%ip)

    @app.route('/favicon.ico/')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

    print(app.url_map)

    return app
