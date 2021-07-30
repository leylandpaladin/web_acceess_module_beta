# web_acceess_module_beta

Структура проекта:



модули:

- __init__.py - Задает настройки фласка и подгружает блупринты
- auth.py - Содержит в себе руты связанные с логином и авторизацией
- Database.py - модуль для манипулирования базой данных через ORM
- Forms.py - WTForms, в HTML подгружается с помощью Jinja2
- index.py - Хоум пейж
- models.py - Модели БД для авторизации
- profile.py - руты и функции которые видны только после логина

- main.py - запускает все вышеописанное.


Структура:

Сначала открывает index.html > оттуда можно логинится, после логина открывается profile_+id пользователя, оттуда и доступно все остальное.


Библиотеки:

- Flask
- Flask-security
- FlaskWTF
- WTForms
- SQLAlchemy
- mariadb и maria_db_connector c/


OpenVPN:

Старт сервиса с нормальным конфигом 

- systemctl start openvpn@server 

Генерация Серта 

- cd /etc/openvpn/easy-rsa 
- ./easyrsa build-client-full VD-RPI-1 nopass
