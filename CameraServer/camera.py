from datetime import datetime
import random
from PIL import Image
import cv2

live_feed = cv2.VideoCapture(0)  # Access camera at port 0


def get_image():
    ret, frame = live_feed.read()  # Read current frame from camera
    return frame


def take_photo():
    print("Creating file")
    cam_image = get_image()  # Take photo
    file = 'images/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png"    # Create file to store image
    cv2.imwrite(file, cam_image)  # Write image data to file


def close_camera():
    print("Closing camera")
    live_feed.release()
    cv2.destroyAllWindows()
