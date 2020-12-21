import socket 
import os
from _thread import *


ServerSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print("Listen... ")
ServerSocket.listen(5)

def Multi_threaded_client(connection):
    connection.send(str.encode('Server is working'))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()

while True:
    Client, addr = ServerSocket.accept()
    print("Connected to: " + addr[0] + ": " + str(addr[1]))
    start_new_thread(Multi_threaded_client, (Client, ))
    ThreadCount += 1
    print("Thread number: ", str(ThreadCount))
ServerSocket.close()