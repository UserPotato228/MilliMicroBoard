from flask import Blueprint

bp = Blueprint("themes", __name__)
from app.themes import routes
