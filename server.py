import socket
from _thread import *
import sys

serverPort = 9999
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Create socket failed: %s" % e)
    sys.exit(1)

clients = []

try:
    serverSocket.bind(('localhost', serverPort))
except socket.error as e:
    print("Error binding socket to the port: %s" %e )
    sys.exit(1)

print('Waiting for connection ...')
serverSocket.listen(2)

def game_thread():
    board = "-/-/-/-/-/-/-/-/-"
    player_x = clients[0]
    player_o = clients[1]
    

    player_x.send("X".encode('utf-8'))
    print("X: " + player_x.recv(2048).decode('utf-8'))
    player_o.send("O".encode('utf-8'))
    print("O: " + player_o.recv(2048).decode('utf-8'))

    while True:
        player_x.send(board.encode('utf-8'))
        print("X: " + player_x.recv(2048).decode('utf-8'))
        player_o.send(board.encode('utf-8'))
        print("O: " + player_o.recv(2048).decode('utf-8'))

while len(clients) != 2:
    try:
        connectionSocket, addr = serverSocket.accept()
        print('\nConnection established with: ' + addr[0] + ':' + str(addr[1]))
        # start_new_thread(threaded_client, (connectionSocket, ))
        clients.append(connectionSocket)
    except socket.error as e:
        print("\nError Establishing connection: %s" % e)

start_new_thread(game_thread, ())

while True:
    a = 1

connectionSocket.close()