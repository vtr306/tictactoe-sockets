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

def checkWin(arr):
    if((arr[0] == arr[2] and arr[2] == arr[4]) and arr[0] != '-' ):
        return True
    elif((arr[6] == arr[8] and arr[8] == arr[10]) and arr[6] != '-'):
        return True
    elif((arr[12] == arr[14] and arr[14] == arr[16]) and arr[12] != '-'):
        return True
    elif((arr[0] == arr[6] and arr[6] == arr[12]) and arr[0] != '-'):
        return True
    elif((arr[2] == arr[8] and arr[8] == arr[14]) and arr[2] != '-'):
        return True
    elif((arr[4] == arr[10] and arr[10] == arr[16]) and arr[4] != '-'):
        return True
    elif((arr[0] == arr[8] and arr[8] == arr[16]) and arr[0] != '-'):
        return True
    elif((arr[4] == arr[8] and arr[8] == arr[12]) and arr[4] != '-'):
        return True

    return False

def tictactoe():
    boardstring = "-/-/-/-/-/-/-/-/-"
    board = list(boardstring)
    player_x = clients[0]
    player_o = clients[1]
    

    player_x.send("X".encode('utf-8'))
    print("X: " + player_x.recv(2048).decode('utf-8'))
    player_o.send("O".encode('utf-8'))
    print("O: " + player_o.recv(2048).decode('utf-8'))

    while True:
        player_x.send(boardstring.encode('utf-8'))
        play_x = int(player_x.recv(2048).decode('utf-8'))
        print("X: " + str(play_x))
        board[2*play_x - 2] = 'X'
        if (checkWin(board)):
            result = "X Won"
            print(result)
            for client in clients:
                client.send(result.encode('utf-8'))
            break
        boardstring =  ''.join(str(item) for item in board)
        player_o.send(boardstring.encode('utf-8'))
        play_o = int(player_o.recv(2048).decode('utf-8'))
        print("O:" + str(play_o))
        board[2*play_o - 2] = 'O'
        boardstring =  ''.join(str(item) for item in board)
        if (checkWin(board)):
            result = "O Won"
            print(result)
            for client in clients:
                client.send(result.encode('utf-8'))
            break
    

while len(clients) != 2:
    try:
        connectionSocket, addr = serverSocket.accept()
        print('\nConnection established with: ' + addr[0] + ':' + str(addr[1]))
        clients.append(connectionSocket)
    except socket.error as e:
        print("\nError Establishing connection: %s" % e)

tictactoe()

connectionSocket.close()