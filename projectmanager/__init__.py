import os

CHARACTERS_ROOT = "D:/ProjectManager-Template/assets/characters/"
PROPS_ROOT = "D:/ProjectManager-Template/assets/props/"
ENVIRONMENTS_ROOT = "D:/ProjectManager-Template/assets/environments/"
SHOT_ROOT = "D:/ProjectManager-Template/shots/"


def _list_folders(root):
    folders = list()
    root_items = os.listdir(root)

    for item in root_items:
        if os.path.isdir(root + item):
            folders.append(item)

    return folders


def all_tasks(character = ""):
    pickFolder = CHARACTERS_ROOT + character + "/"
    return _list_folders(str(pickFolder))


def all_characters():
    return _list_folders(CHARACTERS_ROOT)


def all_props():
    return _list_folders(PROPS_ROOT)


def all_environments():
    return _list_folders(ENVIRONMENTS_ROOT)


def all_shots():
    return _list_folders(SHOT_ROOT)
