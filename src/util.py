import json


def dict_from_json(path) -> dict:
    with open(path) as json_file:
        dictionnaire = json.load(json_file)
        return dictionnaire


print(dict_from_json(r'../ressource/stuff_dd.json').values())
