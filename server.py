# -*- coding: utf-8 -*-

import socket

ip = input('IP: ')

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((ip, 5050))

client = [] # ������ ��� ������ ������ ��������

print ('Server Is Start')
while 1 :
    data, addres = soc.recvfrom(1024)
    print(addres[0], addres[1])

    if addres not in client : 
        client.append(addres) # ���� ������ ������� ����, ��������

    for clients in client :
        if clients == addres : 
            continue # �� ���������� ������ �������, ������� �� �������
        soc.sendto(data, clients)
