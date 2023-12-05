import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

homepage_content_panel = None
OwnProjects_content_panel = None

def set_panel(panel, form):
  panel.clear()
  panel.add_component(form)

