from flask import Blueprint

bp = Blueprint("thread", __name__)
from app.thread import routes
