"""Processes image before classification
Returns image data after processing

For now, takes an image and makes it gray-scale
"""

import cv2


def process_image(file):
    print("Processing")
    image = cv2.imread(file)
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return processed_image  # Returns numpy.ndarray
