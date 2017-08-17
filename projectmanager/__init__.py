import os

PROJECT_ROOT = "D:/ProjectManager-Template"
ASSET_FOLDER = "assets"
SHOT_FOLDER = "shots"
WIP_FOLDER = "wip"


def _list_folders(root):
    folders = list()
    try:
        root_items = os.listdir(root)
    except WindowsError:
        return list()

    for item in root_items:
        if os.path.isdir(os.path.join(root, item)):
            folders.append(item)

    return folders


def _list_files(root):
    files = list()
    root_items = os.listdir(root)

    for item in root_items:
        if os.path.isfile(os.path.join(root, item)):
            files.append(item)

    return files


def all_asset_types():
    assets_folder = os.path.join(
        PROJECT_ROOT,
        ASSET_FOLDER
    )
    return _list_folders(assets_folder)


def all_assets(asset_type):
    asset_types_folder = os.path.join(
        PROJECT_ROOT,
        ASSET_FOLDER,
        asset_type
    )
    return _list_folders(asset_types_folder)


def all_tasks(asset_type, asset_name):
    asset_folder = os.path.join(
        PROJECT_ROOT,
        ASSET_FOLDER,
        asset_type,
        asset_name
    )
    return _list_folders(asset_folder)


def last_version(asset_type, asset_name, task_name):
    versions_path = os.path.join(
        PROJECT_ROOT,
        ASSET_FOLDER,
        asset_type,
        asset_name,
        task_name,
        WIP_FOLDER
    )
    versions = _list_files(versions_path)
    return sorted(versions)[-1]


def all_shots():
    shot_folder = os.path.join(
        PROJECT_ROOT,
        SHOT_FOLDER
    )
    return _list_folders(shot_folder)


def all_shot_tasks(shot_number):
    shot_task_folder = os.path.join(
        PROJECT_ROOT,
        SHOT_FOLDER,
        shot_number
    )
    return _list_folders(shot_task_folder)


def last_shot_version(shot_number, task_name):
    shot_version_path = os.path.join(
        PROJECT_ROOT,
        SHOT_FOLDER,
        shot_number,
        task_name,
        WIP_FOLDER
    )
    versions = _list_files(shot_version_path)
    return sorted(versions)[-1]
