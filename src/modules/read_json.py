import json


def read_json(location):
    with open(location, 'r') as fp:
        json_data = json.load(fp)
    return json_data
