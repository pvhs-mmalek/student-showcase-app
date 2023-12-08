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
def get_project_images(project):
  image_files = []
  for id in project['file_ids']:
    image_files.append(app_files.user_images.get_by_id(id))
  return image_files

@anvil.server.callable
def add_project_images(project, image):
  image = app_files.user_images.create_file(image.name, image)
  project['file_ids'] += [image.id]

@anvil.server.callable
def add_project_images(project, image_list):
  for img in image_list:
    image = app_files.user_images.create_file(img.name, img)
    project['file_ids'] += [image.id]

@anvil.server.callable
def delete_project_image(project, image_id):
  app_files.user_images.delete(image_id)
  project['file_ids'] = project['file_ids'].remove(image_id)
  


