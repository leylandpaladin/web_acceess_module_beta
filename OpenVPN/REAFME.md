OpenVPN:

Установка

    apt-get install OpenVPN

Старт сервиса с нормальным конфигом, где server, это файл //etc/OpenVPN/server.config

    systemctl start openvpn@server

Генерация Серта

    cd /etc/openvpn/easy-rsa
    ./easyrsa build-client-full VD-RPI-1 nopass
