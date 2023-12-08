from ._anvil_designer import OwnProjectsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Global
from .ViewOwnProjects import ViewOwnProjects

class OwnProjects(OwnProjectsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    Global.OwnProjects_content_panel = self.content_panel
    self.show_own_projects()

  def show_own_projects(self):
    form = ViewOwnProjects()
    self.content_panel.clear()
    self.content_panel.add_component(form)



