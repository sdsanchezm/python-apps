from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secretkey21'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


#TF:K0vSCCAM2ss
# PEP 8 Documentation
# https://www.python.org/dev/peps/pep-0008/
# no dash in the name of the module
# gotta call the function that is used to create the app
# in python:
# import from flask_logins_1 import db, create_app
# db.create_all(app=create_app())
# Environment documentation:
# https://flask.palletsprojects.com/en/1.1.x/cli/ 
# flask init documentation
# https://flask-login.readthedocs.io/en/latest/#module-flask_login
