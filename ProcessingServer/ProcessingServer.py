"""Instantiates an FTP server to receive images, and an HTTP client to send classification data

"""

import threading
import time
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import cv2


import logging
import ImagePreprocessing
import HTTPClient
import DataStorage
import ImageMetadata
import TCP_Client
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
        print("Received %s from %s" % (file, self.username))
        file_name = ImageMetadata.get_file_name(file)
        # Create folder to hold pre-processed image and JSON
        folder_name = "data_processed\\%s" % file_name
        os.mkdir(folder_name)
        pre_processed_image = ImagePreprocessing.process_image(file)
        cv2.imwrite('data_processed\\%s\\%s.png' % (file_name, file_name), pre_processed_image)
        DataStorage.create_json("Unknown", -1, ImageMetadata.get_date_taken(file_name), folder_name + "\\" + file_name + ".json")



    def on_incomplete_file_received(self, file):
        print("Received incomplete file from %s" % self.username)

    def on_incomplete_file_sent(self, file):
        print("%s Sent incomplete file" % self.username)


def start_ftp():
    print("Starting FTP")
    authorizer = DummyAuthorizer()
    authorizer.add_user("webcam", "1234", "./data_received", perm="lw")
    handler = ProcessingHandler
    handler.authorizer = authorizer
    server = FTPServer(('0.0.0.0', 21), handler)
    logging.basicConfig(filename='./log/pyftpd.log', level=logging.INFO)  # Store FTP server log
    server.serve_forever()

if __name__ == "__main__":
    ftp_server_thread = threading.Thread(target=start_ftp, args=())
    ftp_server_thread.start()

    tcp_client_thread = threading.Thread(target=TCP_Client.main())
    tcp_client_thread.start()








