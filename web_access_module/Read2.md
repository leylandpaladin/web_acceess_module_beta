################################
Старт сервиса с нормальным конфигом
################################
systemctl start openvpn@server #server - server.cfg из корня /etc/openvpn/

################################
Генерация Серта
################################
cd /etc/openvpn/easy-rsa
./easyrsa build-client-full VD-RPI-1 nopass
