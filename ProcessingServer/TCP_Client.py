

from socket import *
import sys

server_name = 'localhost'

server_port = 1234


def send_message(message):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    client_socket.send(message.encode())
    client_socket.close()
