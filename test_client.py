import socket
import random, string, time 
import json

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

print('Waiting for connection response')
# start_time = time.time()
try:
    ClientMultiSocket.connect((host, port))
    # client2 = ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)

def data():
    values = {}
    count = 0
    
    while count < 10:
        value1 = int(random.randint(1, 100))
        value2 = [''.join(random.choice(string.ascii_letters) for _ in range(3))]
        values[value1] = value2
        count += 1

    return values


while True:
    # values = data()
    data = json.dumps(data())
    ClientMultiSocket.send(data.encode())
    # client2.send()
    res = ClientMultiSocket.recv(1024)

    print(res.decode('utf-8'))

ClientMultiSocket.close()