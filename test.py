import projectmanager

PROJECT_NAME = "ProjectManager-Template"

#
# User Story #1 : ETQ graphiste, je souhaite trouver la derniere version de mon travail

# Choix "Asset"
asset_types = projectmanager.all_asset_types(project_name=PROJECT_NAME)

# Choix "Characters"
characters = projectmanager.all_assets(project_name=PROJECT_NAME, asset_type="characters")

# Choix "Pierre"
asset_tasks = projectmanager.all_tasks(project_name=PROJECT_NAME, asset_type="characters", asset_name="pierre")

# Choix "Modeling"
last_asset_version = projectmanager.last_version(project_name=PROJECT_NAME, asset_type="characters", asset_name="pierre", task_name="modeling")

# Choix "Shot"
shots = projectmanager.all_shots(project_name=PROJECT_NAME)

# Choix "Task"
shot_tasks = projectmanager.all_shot_tasks(project_name=PROJECT_NAME, shot_number="p001")

# Choix "Dernier Shot"
last_shot_version = projectmanager.last_shot_version(project_name=PROJECT_NAME, shot_number="p001", task_name="animation")

#
# User Story #2 : ETQ Graphiste, je souhaite pouvoir ajouter un asset facilement
projectmanager.create_asset(project_name=PROJECT_NAME, asset_type="characters", asset_name="jean")
projectmanager.create_tasks(project_name=PROJECT_NAME, asset_type="characters", asset_name="jean", task_name="lighting")
