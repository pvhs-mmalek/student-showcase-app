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
    current_user['projects'] = [app_tables.projects.add_row(email=current_user['email'], images=[])]
  else:
    current_user['projects'] += [app_tables.projects.add_row(email=current_user['email'], images=[])]

@anvil.server.callable
def update_project(project, project_dict):
  if app_tables.projects.has_row(project):
    project.update(**project_dict)
  else:
    raise Exception('Project does not exist')

@anvil.server.callable
def update_project(project, project_dict, image_list):
  if app_tables.projects.has_row(project):
    project.update(**project_dict)
    for i in project['images']:
      i.delete()
    project['images'] = []
    for b in image_list:
      print(project['images'])
      print(b)
      project['images'] += [app_tables.images.add_row(image=b)]
  else:
    raise Exception('Project does not exist')

@anvil.server.callable
def check_project_images(project):
  if project['images'] == None:
    project['images'] = []

@anvil.server.callable
def get_project_images(project):
  img_list = []
  for img in project['images']:
    img_list += [img['image'].get_bytes()]
  return img_list



