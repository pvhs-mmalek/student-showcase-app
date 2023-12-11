import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

homepage_content_panel = None
OwnProjects_content_panel = None
OwnProjects_repeating_panel = None
own_img_list = []
current_project = None
edit_image_panel = None
own_projects = None
own_profile = None
selected_profile = None

def set_panel(panel, form):
  panel.clear()
  panel.add_component(form)
