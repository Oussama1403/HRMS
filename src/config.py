"""Flask configuration."""

import os

SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
