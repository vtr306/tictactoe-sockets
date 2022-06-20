import socket
from _thread import *
import sys

serverPort = 9999

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Create socket failed: %s" % e)
    sys.exit(1)

try:
    clientSocket.connect(('localhost', serverPort))
except socket.gaierror as e:
    print("Address-related error: %s" % e)
    sys.exit(1)
except socket.error as e:
    print("Error connecting to server: %s" % e)
    sys.exit(1)

print("Server Connection Accepted")

try:
    print("You are: " + clientSocket.recv(2048).decode('utf-8'))
    clientSocket.send("OK".encode('utf-8'))
except socket.error as e:
    print(e)

while True:
    try:
        data = clientSocket.recv(2048).decode('utf-8')
        if (data == "O Won" or data == "X Won" or data == "We Tied"):
            print(data)
            datafinish = clientSocket.recv(2048).decode('utf-8')
            datafinish = datafinish.split('/')
            print(datafinish[0:3])
            print(datafinish[3:6])
            print(datafinish[6:9])
            break
        data = data.split('/')
        print(data[0:3])
        print(data[3:6])
        print(data[6:9])
        while True:
            play = int(input("Choose your move (1-9): "))
            if data[play-1] == '-':
                clientSocket.send(str(play).encode('utf-8'))
                break
            else:
                print("Invalid Move")
    except socket.error as e:
        print(e)

clientSocket.close()
print("Server Connection closed")