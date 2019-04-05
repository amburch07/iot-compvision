from socket import *
import sys

server_socket = socket(AF_INET, SOCK_STREAM)

server_port = 1234

server_socket.bind(("", server_port))

server_socket.listen(1)  # Listen to at most 1 connection at a time

print("Serving at port %s" % server_port)

while True:
    connection_socket, addr = server_socket.accept()
    try:
        print("Received connection from ", addr)
        connection_socket.close()

    except IOError:
        print("Error")
        connection_socket.close()

