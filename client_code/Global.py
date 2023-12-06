import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

homepage_content_panel = None
OwnProjects_content_panel = None
own_image_index = 0
own_img_list = []
own_img = None

def set_panel(panel, form):
  panel.clear()
  panel.add_component(form)

def update_own_image(item):
  own_img_list = anvil.server.call('get_project_images', self.item)
  own_img = img_list[own_image_index]

