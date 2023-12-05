from ._anvil_designer import OwnProjectsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Global
from ...ProjectView import ProjectView
from .ViewOwnProjects import ViewOwnProjects

class OwnProjects(OwnProjectsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def show_own_projects(self):
    form = ViewOwnProjects()
    self.content_panel.clear()
    self.content_panel.add_component(form)



