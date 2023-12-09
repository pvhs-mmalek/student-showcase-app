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

@anvil.server.callable
def get_own_projects():
  current_user = anvil.users.get_user()
  return current_user['projects']

@anvil.server.callable
def add_new_project():
  current_user = anvil.users.get_user()
  if current_user['projects'] == []:
    current_user['projects'] = [app_tables.projects.add_row(email=current_user['email'], filenames=[])]
  else:
    current_user['projects'] += [app_tables.projects.add_row(email=current_user['email'], filenames=[])]

@anvil.server.callable
def update_project(project, project_dict):
  if app_tables.projects.has_row(project):
    project.update(**project_dict)
  else:
    raise Exception('Project does not exist')

@anvil.server.callable
def update_project(project, project_dict):
  if app_tables.projects.has_row(project):
    project.update(**project_dict)
  else:
    raise Exception('Project does not exist')

@anvil.server.callable
def get_images(image_id_list):
  image_files = []
  for id in image_id_list:
    image_files.append(app_files.user_images.get_by_id(id))
  return image_files

@anvil.server.callable
def get_image(image_id):
  return app_files.user_images.get_by_id(image_id)

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
def delete_project_image(project, image_id):
  file = app_files.user_images.get_by_id(image_id)
  file.delete()
  project['file_ids'].remove(image_id)
  if project['file_ids'] == None:
    project['file_ids'] = []

@anvil.server.callable
def replace_image_file(project, old_image_id, new_image):
  delete_project_image(project, old_image_id)
  add_project_image(project, new_image)
  


