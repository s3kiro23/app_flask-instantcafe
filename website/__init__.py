from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "M@y2o22!"

    # Routes
    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)
    app.static_folder = 'static'

    # Database

    return app
