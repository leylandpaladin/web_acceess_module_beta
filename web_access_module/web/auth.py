from flask import Blueprint,render_template, request, flash
from . import Forms
from . import Database
from . import db
from . import models
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def login_form():
    login_form = Forms.LoginForm()

    if login_form.validate_on_submit():

        login = login_form.login.data
        print(login)
        password = login_form.password.data
        print(password)
        user = models.User.query.filter_by(Login=login).first()
        print(user)

        if user:
            if check_password_hash(user.Password, password):
                return "<h1> залогинен <h1>"

            else:
                return '<h1> чето-не так <h1>'
        if user == None:
            return '<h1> fisting <h1>'
    return render_template('login.html', login_form=login_form)


@auth.route('/add_customer', methods=['GET', 'POST'])
def add_customer_form():
    add_customer_form = Forms.AddToDBForm()

    if add_customer_form.validate_on_submit():

        Database.add_customer(Login=add_customer_form.login.data,
                              FIO=add_customer_form.name.data,
                              Password=add_customer_form.password.data,
                              Phone_number=add_customer_form.phone.data)

        return '<h1> Клиент добавлен в базу данных <h1>'

    return render_template('sign.html', add_customer_form=add_customer_form)


