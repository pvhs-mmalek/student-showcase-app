from ._anvil_designer import ViewOwnProjectsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .NewProjectAlert import NewProjectAlert


class ViewOwnProjects(ViewOwnProjectsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.own_projects_panel.items = anvil.server.call('get_own_projects')

  def new_project_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    save_clicked = alert(content = NewProjectAlert(), buttons=[('')])
    
