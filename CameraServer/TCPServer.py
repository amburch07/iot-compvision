from socket import *
import sys
import ftp_camera_client

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
                message = message.strip()
                print("Received message ", message)
                if(message=="{start}"):
                    print("Taking photo")

        except IOError:
            connection_socket.close()
            print("Closing")
    serverSocket.close()
    sys.exit()

if __name__ == '__main__':
    start_server()
