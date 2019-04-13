"""Creates JSON file containing classification data

"""

import json


JSON_DATA = {
    'classification': 'none',
    'confidence': 0
    }

def create_json(classification, confidence, file_name):
    data = JSON_DATA
    data['classification'] = classification
    data['confidence'] = confidence
    print(data)
    with open(file_name, 'w') as write_file:
        json.dump(data, write_file)
