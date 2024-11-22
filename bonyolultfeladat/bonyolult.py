import json

def beolvas(file):
    with open(file, "r") as f:
        return json.load(f)