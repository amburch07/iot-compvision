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





def create_json(information, file_name):
    data = dict.fromkeys(['year', 'month', 'day', 'hour', 'minute', 'second'])
    index = 0
    for key, value in data.items():
        data[key] = information[index]
        index = index + 1
    print(data)
    with open(file_name + ".json", 'w') as outfile:
        json.dump(data, outfile)

