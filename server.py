# -*- coding: utf-8 -*-

import socket

ip = input('IP: ')
port = int(input('PORT: '))

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((ip, port))

client = [] #Массив где храним адреса клиентов

print ('Server Is Start')

while 1 :
    data, addres = soc.recvfrom(1024)
    print(addres[0], addres[1])

    if addres not in client : 
        client.append(addres) #Если такого клиента нету, добавить

    for clients in client :
        if clients == addres : 
            continue #Не отправлять данные клиенту, который их прислал
        soc.sendto(data, clients)
