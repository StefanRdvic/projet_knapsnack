import json


def dict_from_json(path) -> dict:
    with open(path) as json_file:
        dictionnaire = json.load(json_file)
        return dictionnaire


def get_item_info(item, objects_dict) -> (int, int):
    return objects_dict[item][0], objects_dict[item][1]


print(dict_from_json(r'../ressource/stuff_dd.json').values())
