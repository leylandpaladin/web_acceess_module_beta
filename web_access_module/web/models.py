
from flask_login import UserMixin
from flask_security import Security, SQLAlchemyUserDatastore
from . import db

roles_users = db.Table('roles_users',
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                    db.Column('role_id', db.Integer, db.ForeignKey('role.id')))

class User(db.Model, UserMixin):
    __tablename__ = 'Customers'
    id = db.Column(db.Integer, primary_key=True)
    Login = db.Column(db.String(150), unique=True)
    Password = db.Column(db.String(length=100))


class Role(db.Model):
    __tablename__ = "Roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(500))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)


