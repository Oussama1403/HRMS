"""Bundle all sections and expose the Flask APP"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)

app.config.from_pyfile('./config.py')

db = SQLAlchemy(app)


app.config['SESSION_SQLALCHEMY'] = db

from .models import *

from .auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint,url_prefix='/auth')

from .admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint,url_prefix='/admin')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

with app.app_context(): #solves: RuntimeError(unbound_message) from None RuntimeError: Working outside of application context.
    db.create_all() # create DB.

from .routes import *



