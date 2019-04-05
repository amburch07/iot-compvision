"""Instantiates an FTP server to receive images, and an HTTP client to send classification data

"""

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging
import ImagePreprocessing
import HTTPClient
import requests
import json

class ProcessingHandler(FTPHandler):
    def on_connect(self):
        print("%s:%s connected" % (self.remote_ip, self.remote_port))

    def on_disconnect(self):
        print("%s Disconnected" % self.username)

    def on_login(self, username):
        print("%s has logged in" % username)

    def on_logout(self, username):
        print("%s has logged out" % username)

    def on_file_sent(self, file):
        print("%s has sent %s " % (self.username, file))

    def on_file_received(self, file):
        start_http_client()
        print("Received %s from %s" % (file, self.username))
        ImagePreprocessing.process_image(file)

    def on_incomplete_file_received(self, file):
        print("Received incomplete file from %s" % self.username)

    def on_incomplete_file_sent(self, file):
        print("%s Sent incomplete file" % self.username)


def start_ftp():
    authorizer = DummyAuthorizer()
    authorizer.add_user("webcam", "1234", "./data_received", perm="lw")
    handler = ProcessingHandler
    handler.authorizer = authorizer
    server = FTPServer(('0.0.0.0', 21), handler)
    logging.basicConfig(filename='./log/pyftpd.log', level=logging.INFO)  # Store FTP server log
    server.serve_forever()


def start_http_client():
    HTTPClient.post_request()



if __name__ == "__main__":
    start_ftp()






