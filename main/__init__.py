from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db=SQLAlchemy()
bcrypt=Bcrypt()
cors=CORS()

def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:22061998@localhost/friendbook'
    db.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)

    from .controllers.user_controller import user_route
    app.register_blueprint(user_route, url_prefix='/users')
    return app

