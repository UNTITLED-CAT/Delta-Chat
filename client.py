# -*- coding: utf-8 -*-

#����������� ������ ������
import socket
import threading

#��������� ���������
def get_msg():
    while 1 :
        data = soc.recv(1024)
        print(data.decode('utf-8'))

ip = input('IP: ')
port = int(input('PORT:'))

server = ip, port
alias = input('Alias') #���� ����������
soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soc.bind(('', 0)) #������ ����� ��� ������
soc.sendto((alias+' Connect to server').encode('utf-8'), server) #��������� ���� � �����������
flow = threading.Thread(target=get_msg) #������� �����
flow.start()

while 1 :
    message = input()
    soc.sendto(('['+alias+']: '+message).encode('utf-8'), server) #�������� ���������
