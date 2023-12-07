import anvil.files
from anvil.files import data_files
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
    current_user['projects'] = [app_tables.projects.add_row(email=current_user['email'])]
  else:
    current_user['projects'] += [app_tables.projects.add_row(email=current_user['email'])]

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
def set_project_images(project, image_list):
  if app_tables.projects.has_row(project):
    for f in project['files']:
      f.delete()
    for img in image_list:
      project['files'] += [app_tables.files.add_row(file=img)]

@anvil.server.callable
def return_image_from_file():
  pass

