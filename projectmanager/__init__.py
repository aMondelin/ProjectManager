import os

ASSET_ROOT = "D:/"
SHOT_ROOTS = "D:/"


def _list_folders(root):
    folders = list()
    root_items = os.listdir(root)

    for item in root_items:
        if os.path.isdir(root + item):
            folders.append(item)

    return folders


def all_assets():
    return _list_folders(ASSET_ROOT)


def all_shots():
    return _list_folders(SHOT_ROOTS)
