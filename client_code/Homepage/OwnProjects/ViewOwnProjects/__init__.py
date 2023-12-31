from ._anvil_designer import ViewOwnProjectsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .... import Global


class ViewOwnProjects(ViewOwnProjectsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.own_projects_panel.items = anvil.server.call('get_own_projects')
    Global.OwnProjects_repeating_panel = self.own_projects_panel

  def new_project_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    save_clicked = alert(title='Create new project?', buttons=[('Cancel', False), ('Confirm', True)])
    if save_clicked:
      anvil.server.call('add_new_project')
      Global.set_panel(Global.OwnProjects_content_panel, ViewOwnProjects())
      
    
