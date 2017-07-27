import projectmanager


characters = projectmanager.all_characters()
props = projectmanager.all_props()
environments = projectmanager.all_environments()
shots = projectmanager.all_shots()

getCharacter = "pierre"
tasks = projectmanager.all_tasks(getCharacter)

print "\n".join(tasks)


# print "\n".join(characters)
# print "\n".join(shots)
