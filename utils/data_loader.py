import json


def load_test_data(filepath):
    file = open(filepath, 'r')
    data = json.load(file)
    return data