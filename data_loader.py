import json

def load_dataset(file_path):
    with open(file_path, 'r') as file:
        dataset = json.load(file)
    return dataset