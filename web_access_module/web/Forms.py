from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField


class LoginForm(FlaskForm):

    login = StringField('Email')
    password = PasswordField('Пароль')


class AddToDBForm(FlaskForm):

    login = StringField('Email')
    name = StringField('ФИО')
    password = PasswordField('Пароль')
    phone = IntegerField('Номер телефона')
