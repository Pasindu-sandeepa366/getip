#!/usr/bin/python3
import socket
from os import system

ip = '127.0.0.1'
port = 6969

response = '''\
HTTP/1.1 200 OK

<html>
    <head>
        <title>Python<3</title>
    </head>

    <body>
   <?php
    header('Location: https://www.google.com/');
    exit
    ?>
    </body>
</html>
'''

print(f'http://{ip}:{port}')

sk =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind((ip,port))
try:
    while True:
        sk.listen()
        conn,addr=sk.accept()
        print(f'conn {conn}')
        print(f'addr {addr}')

        
        breq = conn.recv(1024).decode('utf-8')
        print(breq)
        print(f'connected : {addr}')

        conn.send(response.encode('utf-8'))
        conn.close()
    #        break;
except KeyboardInterrupt:
    sk.close()
    print('User quit programe')