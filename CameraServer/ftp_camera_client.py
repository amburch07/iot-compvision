from ftplib import FTP
import time
import camera
import os

ftp = FTP('')


def connect_to_server(host, port):
    ftp.connect(host, port)
    ftp.login(user="webcam", passwd="1234")


def send_file():
    while True:
        camera.take_dummy_photo()  # Take photo and store it in the /images directory
        image_list = os.listdir('images')
        most_recent = open('images/' + image_list[-1], 'rb')
        ftp.storbinary('STOR ' + most_recent.name[7:], most_recent)
        time.sleep(5)  # Wait five seconds before taking and sending next photo



if __name__ == "__main__":
    connect_to_server('localhost', 21)
    send_file()
