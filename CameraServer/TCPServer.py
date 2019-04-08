from socket import *
import sys
import cv2



server_socket = socket()

def start_server():
    print("Starting TCP")
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', 1234))
    server_socket.listen(1)
    while True:
        connection_socket, addr = server_socket.accept()
        try:
            print("Connection: received from client at ", addr)
            while True:
                message = connection_socket.recv(1024).decode('utf-8')
                if (len(message) > 0):
                    print("Message received: " + message)
                    if message == "{quit}":
                        print("Quit requested")
                        connection_socket.close()
                        break
                    if message == "{start}":
                        print("Sending photos")
        except IOError:
            connection_socket.close()
            print("Closing")
    serverSocket.close()
    sys.exit()

def run():
    print("In run")

