from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://admin:Doska777@35.224.130.4:3306/testdb'
    app.secret_key = 'GOWNO'
    db.init_app(app)

    from .auth import auth
    from .index import index
    from .profile import profile

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(profile, url_prefix='/profile')

    return app
