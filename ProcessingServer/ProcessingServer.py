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

import DataStorage
import ImageMetadata

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

        os.system(
            "py classify/src/align/align_dataset_mtcnn.py classify/datasets/test_pi classify/datasets/test_pi_clean")
        os.system(
            "py classify/src/classifier.py CLASSIFY classify/datasets/test_pi_clean classify/models/20180408-102900.pb classify/models/classifier.pkl > classify/output.txt")



        #retreive classification info
        with open("classify\\output.txt") as f:
            lines = f.readlines()
        info = lines[-2].split()[1:]
        info = [info[0]+'_'+info[1], info[-1]]

        #folder to hold pre-processed image and JSON
        folder_name = "Classify\\datasets\\test_pi_clean\\%s" % file_name
        os.mkdir(folder_name)
        DataStorage.create_json(info[0], info[1], ImageMetadata.get_date_taken(file_name), folder_name + "\\" + file_name + ".json")

        #now json is created


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
    logging.basicConfig(filename='./log\\pyftpd.log', level=logging.INFO)  # Store FTP server log
    server.serve_forever()

if __name__ == "__main__":
    ftp_server_thread = threading.Thread(target=start_ftp, args=())
    ftp_server_thread.start()

