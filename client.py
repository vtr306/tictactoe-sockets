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
        print(data.split('/'))
        play = input("Choose your move: ")
        clientSocket.send(play.encode('utf-8'))
    except socket.error as e:
        print(e)

clientSocket.close()
print("Server Connection closed")