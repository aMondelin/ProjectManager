import os

PROJECT_ROOT = "C:"
DROPBOX_FOLDER = "Dropbox"
ASSET_FOLDER = "assets"
SHOT_FOLDER = "shots"
WIP_FOLDER = "wip"
IMAGES_FOLDER = "img"
DEFAULT_TASKS = ["concept", "maps", "modeling", "rig"]
ICON_NAME = '_icon_manager.jpg'


def _make_project_root(project_name):
    project_root = os.path.expandvars('$USERPROFILE')
    return os.path.join(project_root, DROPBOX_FOLDER, project_name)


def _icon_root(project_name):
    icon_folder = make_images_root(project_name)
    return os.path.join(icon_folder, ICON_NAME)


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


def make_images_root(project_name):
    image_root = _make_project_root(project_name)
    return os.path.join(image_root, IMAGES_FOLDER)


def make_asset_root(project_name, asset_type, asset_name):
    project_root = _make_project_root(project_name)
    return os.path.join(project_root, ASSET_FOLDER, asset_type, asset_name)


def make_task_root(project_name, asset_type, asset_name, asset_task):
    asset_root = make_asset_root(project_name, asset_type, asset_name)
    return os.path.join(asset_root, asset_task)


def all_asset_types(project_name):
    project_root = _make_project_root(project_name)
    assets_folder = os.path.join(
        project_root,
        ASSET_FOLDER
    )
    return _list_folders(assets_folder)


def all_assets(project_name, asset_type):
    project_root = _make_project_root(project_name)
    asset_types_folder = os.path.join(
        project_root,
        ASSET_FOLDER,
        asset_type
    )
    return _list_folders(asset_types_folder)


def all_tasks(project_name, asset_type, asset_name):
    asset_folder = make_asset_root(project_name, asset_type, asset_name)
    return _list_folders(asset_folder)


def asset_versions(project_name, asset_type, asset_name, asset_task):
    task_root = make_task_root(project_name, asset_type, asset_name, asset_task)
    versions_path = os.path.join(
        task_root,
        WIP_FOLDER
    )
    return _list_files(versions_path)


def last_version(project_name, asset_type, asset_name, task_name):
    versions = asset_versions(project_name, asset_type, asset_name, task_name)
    return sorted(versions)[-1]


def all_shots(project_name):
    project_root = _make_project_root(project_name)
    shot_folder = os.path.join(
        project_root,
        SHOT_FOLDER
    )
    return _list_folders(shot_folder)


def all_shot_tasks(project_name, shot_number):
    project_root = _make_project_root(project_name)
    shot_task_folder = os.path.join(
        project_root,
        SHOT_FOLDER,
        shot_number
    )
    return _list_folders(shot_task_folder)


def last_shot_version(project_name, shot_number, task_name):
    project_root = _make_project_root(project_name)
    shot_version_path = os.path.join(
        project_root,
        SHOT_FOLDER,
        shot_number,
        task_name,
        WIP_FOLDER
    )
    versions = _list_files(shot_version_path)
    return sorted(versions)[-1]


def create_wip_folder(task_root):
    if os.path.exists(task_root):
        os.mkdir(os.path.join(task_root,WIP_FOLDER))


def create_asset(project_name, asset_type, asset_name, tasks=DEFAULT_TASKS):
    asset_root = make_asset_root(project_name, asset_type, asset_name)

    if not os.path.exists(asset_root):
        os.mkdir(asset_root)

        for task in tasks:
            task_root = make_task_root(project_name, asset_type, asset_name, task)
            if not os.path.exists(task_root):
                os.mkdir(task_root)
                create_wip_folder(task_root)

    else:
        print 'This asset already exist.'


def create_tasks(project_name, asset_type, asset_name, task_name):
    asset_root = make_asset_root(project_name, asset_type, asset_name)

    if os.path.exists(asset_root):
        task_root = make_task_root(project_name, asset_type, asset_name, task_name)
        if not os.path.exists(task_root):
            os.mkdir(task_root)
            create_wip_folder(task_root)

    else:
        print 'This task already exist.'


def file_extension(file_root):
   return os.path.splitext(file_root)[1]