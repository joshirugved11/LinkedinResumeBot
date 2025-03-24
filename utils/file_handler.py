import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_credentials():
    return load_json("config/credentials.json")

def get_settings():
    return load_json("config/settings.json")
