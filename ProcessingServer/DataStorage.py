"""Creates JSON file containing classification data

"""

import json


def create_json(information, file_name):
    data = dict.fromkeys(['year', 'month', 'day', 'hour', 'minute', 'second'])
    index = 0
    for key, value in data.items():
        data[key] = information[index]
        index = index + 1
    print(data)
    with open(file_name + ".json", 'w') as outfile:
        json.dump(data, outfile)
