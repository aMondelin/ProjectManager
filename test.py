import projectmanager

#
# User Story #1 : ETQ graphiste, je souhaite trouver la derniere version de mon travail

# Choix "Asset"
asset_types = projectmanager.all_asset_types()

# Choix "Characters"
characters = projectmanager.all_assets(asset_type="characters")

# Choix "Pierre"
asset_tasks = projectmanager.all_tasks(asset_type="characters", asset_name="pierre")

# Choix "Modeling"
last_asset_version = projectmanager.last_version(asset_type="characters", asset_name="pierre", task_name="modeling")

# Choix "Shot"
shots = projectmanager.all_shots()

# Choix "Task"
shot_tasks = projectmanager.all_shot_tasks(shot_number="p001")

# Choix "Dernier Shot"
last_shot_version = projectmanager.last_shot_version(shot_number="p001", task_name="animation")
print last_shot_version

#
# User Story #2 : ETQ Graphiste, je souhaite pouvoir ajouter un asset facilement
projectmanager.create_asset(type_name="characters", name="jean")
projectmanager.create_tasks(type_name="characters", name="jean", task_name=["modeling", "rig"])
