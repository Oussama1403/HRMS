"""Bundle all sections and expose the Flask APP"""

from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_pyfile('./config.py')

db = SQLAlchemy(app)

app.config['SESSION_SQLALCHEMY'] = db

from .models import *

# register blueprints.

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix='/auth')

from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint,url_prefix='/admin')

from .user import user as user_blueprint
app.register_blueprint(user_blueprint,url_prefix='/user')

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

with app.app_context(): #solves: RuntimeError(unbound_message) from None RuntimeError: Working outside of application context.
    db.create_all() # create DB.

# ERROR HANDLING

@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def server_error(error):
    return render_template("errors/500.html"), 500

@app.errorhandler(401)
def access_denied(error):
    return render_template("errors/401.html"), 401    





