# -*- coding: utf-8 -*-

#Импортируем нужные модули
import socket
import threading

#Получение сообщений
def get_msg():
    while 1 :
        data = soc.recv(1024)
        print(data.decode('utf-8'))

ip = input('IP: ')
port = int(input('PORT:'))

server = ip, port
alias = input('Alias') #Ввод псевдонима
soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soc.bind(('', 0)) #Задаем сокет как клиент
soc.sendto((alias+' Connect to server').encode('utf-8'), server) #Оповещаем всех о подключении
flow = threading.Thread(target=get_msg) #Создаем поток
flow.start()

while 1 :
    message = input()
    soc.sendto(('['+alias+']: '+message).encode('utf-8'), server) #отправка сообщения
