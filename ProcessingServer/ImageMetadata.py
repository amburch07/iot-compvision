"""Returns the Year, month, day, hour, second of when photo was taken
Used when storing photo and classification data

"""

import re


class ImageMetadata:

    def get_file_name(file):
        start_of_name = file.rfind('\\') + 1
        end_of_name = len(file) - 4  # Account for '.png'
        file_name = file[start_of_name:end_of_name]
        return file_name

    def get_date_taken(file_name):
        time_taken = re.findall("[0-9]+", file_name)
        return time_taken
