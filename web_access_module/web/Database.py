import sqlalchemy as sqa
from sqlalchemy.ext.declarative import declarative_base
import mariadb
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security,SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from werkzeug.security import generate_password_hash, check_password_hash


db_engine = sqa.create_engine("mariadb+mariadbconnector://admin:Doska777@35.224.130.4:3306/testdb")
Base = declarative_base()

class testdb(Base):
    __tablename__ = 'Customers'
    id = sqa.Column(sqa.Integer, primary_key=True)
    Login = sqa.Column(sqa.String(length=100))
    FIO = sqa.Column(sqa.String(length=100))
    Password = sqa.Column(sqa.String())
    Phone_number = sqa.Column(sqa.String(length=100))


class roles(Base):
    __tablename__ = "Roles"
    id = sqa.Column(sqa.Integer, primary_key=True)
    name = sqa.Column(sqa.String(40))
    description = sqa.Column(sqa.String(500))




Session = sqa.orm.sessionmaker()
Session.configure(bind=db_engine)
Session = Session()


#Base.metadata.create_all(db_engine)

def add_customer(Login, FIO, Password, Phone_number):
    newCustomer = testdb(Login=Login,
                         FIO=FIO,
                         Password=generate_password_hash(password=Password, method='sha256'),
                         Phone_number=Phone_number)

    Session.add(newCustomer)
    Session.commit()
    print('Новый клиент успешно добавлен')



#zaloopa

