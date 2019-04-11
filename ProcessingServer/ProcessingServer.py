"""Instantiates an FTP server to receive images, and an HTTP client to send classification data
"""

import threading
import time
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib import servers
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

        #run classification
        print("Ready to classify")

        os.system("python3 classify/src/align/align_dataset_mtcnn.py classify/datasets/test_pi classify/datasets/test_pi_clean")
        os.system("python3 classify/src/classifier.py CLASSIFY classify/datasets/test_pi_clean classify/models/20180408-102900.pb classify/models/classifier.pkl > classify/output.txt")

        #os.mkdir(folder_name)
        #pre_processed_image = ImagePreprocessing.process_image(file)
        #cv2.imwrite('Classify/datasets/test_pi_clean/%s/%s.png' % (file_name, file_name), pre_processed_image)

        #retreive classification info
        with open("classify/output.txt") as f:
            lines = f.readlines()
        info = lines[-2].split()[1:]
        info = [info[0]+'_'+info[1], info[-1]]

        #folder to hold pre-processed image and JSON
        folder_name = "Classify/datasets/test_pi_clean/%s" % file_name
        DataStorage.create_json(info[0], info[1], ImageMetadata.get_date_taken(file_name), folder_name + "/" + file_name + ".json")

        #now json is created


    def on_incomplete_file_received(self, file):
        print("Received incomplete file from %s" % self.username)

    def on_incomplete_file_sent(self, file):
        print("%s Sent incomplete file" % self.username)

from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler


def start_ftp():
    print("Starting FTP")
    authorizer = DummyAuthorizer()
    authorizer.add_user("webcam", "1234", "./data_received", perm="elrw")
    handler = ProcessingHandler
    handler.authorizer = authorizer
    server = FTPServer(('0.0.0.0', 21), handler)


    #address = ("0.0.0.0", 21)  # listen on every IP on my machine on port 21
    #server = servers.FTPServer(address, FTPHandler)
    #server.serve_forever()

    logging.basicConfig(filename='./log/pyftpd.log', level=logging.INFO)  # Store FTP server log
    server.serve_forever()




if __name__ == "__main__":
    ftp_server_thread = threading.Thread(target=start_ftp, args=())
    ftp_server_thread.start()

    tcp_client_thread = threading.Thread(target=TCP_Client.main())
    tcp_client_thread.start()
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
