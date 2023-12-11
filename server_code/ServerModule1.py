import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

@anvil.server.callable
def check_new_user():
  current_user = anvil.users.get_user()
  if current_user['projects'] == None:
    current_user['projects'] = []
  if current_user['profile'] == None:
    current_user['profile'] = app_tables.profiles.add_row(email=current_user['email'])

@anvil.server.callable
def set_profile_image_id(profile, image_id):
  profile['profile_image'] = image_id

@anvil.server.callable
def set_profile_project_image_id(profile, image_id):
  profile['project_image'] = image_id

@anvil.server.callable
def get_own_projects():
  current_user = anvil.users.get_user()
  return current_user['projects']

@anvil.server.callable
def get_projects_from_email(user_email):
  return app_tables.projects.search(email=user_email)

@anvil.server.callable
def get_profile_by_email(user_email):
  return app_tables.profiles.search(email=user_email)

@anvil.server.callable
def get_own_profile():
  current_user = anvil.users.get_user()
  return current_user['profile']

@anvil.server.callable
def add_new_project():
  current_user = anvil.users.get_user()
  if current_user['projects'] == []:
    current_user['projects'] = [app_tables.projects.add_row(email=current_user['email'], file_ids=[])]
  else:
    current_user['projects'] += [app_tables.projects.add_row(email=current_user['email'], file_ids=[])]

@anvil.server.callable
def update_project(project, project_dict):
  if app_tables.projects.has_row(project):
    project.update(**project_dict)
  else:
    raise Exception('Project does not exist')

@anvil.server.callable
def delete_project(project):
  current_user = anvil.users.get_user()
  if app_tables.projects.has_row(project):
    #daviesian, Anvil Deleloper
    current_user['projects'] = [i for i in current_user['projects'] if i != project]
    delete_all_project_images(project)
    project.delete()
  else:
    raise Exception('project does not exist')

@anvil.server.callable
def add_image_return_id(image):
  file = app_files.user_images.create_file(image.name, image)
  return file.id

@anvil.server.callable
def get_images(image_id_list):
  image_files = []
  for id in image_id_list:
    image_files.append(app_files.user_images.get_by_id(id))
  return image_files

@anvil.server.callable
def get_image(image_id):
  return app_files.user_images.get_by_id(image_id)

def get_images(id_list):
  images = []
  for id in id_list:
    images.append(get_image(id))
  return images

@anvil.server.callable
def get_project_images(project):
  image_files = []
  for id in project['file_ids']:
    image_files.append(app_files.user_images.get_by_id(id))
  return image_files

@anvil.server.callable
def add_project_image(project, image):
  image = app_files.user_images.create_file(image.name, image)
  if project['file_ids'] == None:
    project['file_ids'] = []
  project['file_ids'] += [image.id]

@anvil.server.callable
def add_project_images(project, image_list):
  for img in image_list:
    image = app_files.user_images.create_file(img.name, img)
    project['file_ids'] += [image.id]

@anvil.server.callable
def delete_image(image_id):
  file = app_files.user_images.get_by_id(image_id)
  file.delete()

@anvil.server.callable
def delete_project_image(project, image_id):
  file = app_files.user_images.get_by_id(image_id)
  file.delete()
  print(f'id to delete: {image_id}')
  temp = str(project['file_ids'])
  print(f'server before delete: {temp}')
  project['file_ids'] = [i for i in project['file_ids'] if i != image_id]
  temp = str(project['file_ids'])
  print(f'server after delete: {temp}')
  if project['file_ids'] == None:
    project['file_ids'] = []

@anvil.server.callable
def delete_all_project_images(project):
  if app_tables.projects.has_row(project):
    for i in project['file_ids']:
      file = app_files.user_images.get_by_id(i)
      file.delete()
  else:
    raise Exception('Project does not exist')

@anvil.server.callable
def replace_image_file(project, old_image_id, new_image):
  delete_project_image(project, old_image_id)
  add_project_image(project, new_image)
  
@anvil.server.callable
def update_profile(profile, profile_dict):
  if app_tables.profiles.has_row(profile):
    profile.update(**profile_dict)
  else:
    raise Exception('Profile does not exist')

@anvil.server.callable
def search_profiles_by_name(query):
  result = app_tables.profiles.search()
  if query:
    result = [
      profile for profile in result
      if query in profile['email']
      or query in profile['name']
    ]
  return result

@anvil.server.callable
def advanced_profile_search(query):
  result = app_tables.profiles.search()
  result = []


