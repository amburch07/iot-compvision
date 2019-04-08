"""Creates JSON file containing classification data

"""

import json

JSON_DATA = {
    'classification': 'none',
    'confidence': 0,
    'metadata': {
        'year': 'none',
        'month': 'none',
        'day': 'none',
        'hour': 'none',
        'minute': 'none',
        'second': 'none'
    }
}

def create_json(classification, confidence, date_information, file_name):
    data = JSON_DATA
    data['classification'] = classification
    data['confidence'] = confidence
    data['metadata'] = date_information
    print(data)
    with open(file_name, 'w') as write_file:
        json.dump(data, write_file)



