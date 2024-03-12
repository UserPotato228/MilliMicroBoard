import os
import random

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    MAX_CONTENT_LENGTH = 8 * 1000 * 1000
    ALLOWED_EXTENSIONS = {"webp", "jpg", "jpeg", "png", "gif", "wav", "mp4", "mp3"}
    UPLOAD_FOLDER = os.path.join(base_dir, "app", "static","Img")
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(random.randint(1, 10))
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or 'sqlite:///' + os.path.join(base_dir, "app.db")
