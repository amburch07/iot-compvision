

from socket import *
import sys

server_name = 'localhost'

server_port = 1234

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))


def send_message(message):
    client_socket.send(message.encode())

def main():
    while True:
        message = sys.stdin.readline()
        print("Sending ", message)
        send_message(message + "\r\n")
        sys.stdout.flush()

if __name__ == '__main__':
    main()