import cv2
from datetime import datetime


def process_image(file):  # TODO: Replace with computer-vision code
    print("Processing")
    image = cv2.imread(file)
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Processed/' + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + " MOD.png", processed_image)
    # TODO: Create JSON with image and classification data
    # TODO: Create HTTP client to send JSON data to web server

