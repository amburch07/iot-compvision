from ftplib import FTP
import time
import camera
import os
import threading
import TCPServer


ftp = FTP('')


ftp = FTP('')


def connect_to_server(host, port)       :
    ftp.connect(host, port)
    ftp.login(user="webcam", passwd="1234")


def send_file():
    connect_to_server('localhost', 21)
    print("Sending photo")
    camera.take_photo() # Take photo and store it in the /images directory
    image_list = os.listdir('images')
    most_recent = open('images/' + image_list[-1], 'rb')
    ftp.storbinary('STOR ' + most_recent.name[7:], most_recent)
    return most_recent.name



def close_connection():
    ftp.close()

def main(host, port):
    ftp.connect(host, port)
    ftp.login(user="webcam", passwd="1234")
    send_file()

if __name__ == "__main__":
    ftp_host = 'localhost'
    ftp_port = 21
    try:
        ftp_send = threading.Thread(target=main(ftp_host, ftp_port))
    except IOError:
        print("Could not connect to FTP server!")
    TCPServer.start_server()



