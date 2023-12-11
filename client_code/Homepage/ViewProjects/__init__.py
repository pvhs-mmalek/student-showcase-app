from ._anvil_designer import ViewProjectsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Global

class ViewProjects(ViewProjectsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_project_panel.items = self.item

  def view_user_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    Global.selected_profile.remove_from_parent()
    Global.set_panel(Global.homepage_content_panel, Global.selected_profile)
    
    
