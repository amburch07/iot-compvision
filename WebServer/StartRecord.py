# https://stackoverflow.com/questions/13808187/how-can-i-call-a-specific-function-method-in-a-python-script-from-javascriptjqu


from flask import Flask, render_template, redirect, url_for, request
from flask import make_response


from socket import *
import sys



server_name = 'localhost'
server_port = 1234

app = Flask(__name__)


@app.route('/start', methods=['POST'])
def start_record():
    process_name = request.get('name', None)
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    client_socket.send("Hi".encode())
    client_socket.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
