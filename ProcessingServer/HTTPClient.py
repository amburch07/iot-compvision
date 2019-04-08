"""


"""

import requests
import glob
import os
import glob


def post_request(self):
    try:
        files = glob.glob("./data_received/*.png")
        print(files)
        most_recent_file =  max(files, key=os.path.getctime())
        print("Sending %s" % most_recent_file)
    except IOError:
        print("Error")



def get_request(self):
    pass
