from ._anvil_designer import ViewProfileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ViewProjects import ViewProjects
from ... import Global

class ViewProfile(ViewProfileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    Global.selected_profile = None
    profile_image = self.item['profile_image']
    project_image = self.item['project_image']
    if profile_image != None:
      self.profile_image.source = anvil.server.call('get_image', profile_image)
    if project_image != None:
      self.project_image.source = anvil.server.call('get_image', project_image)


  def show_profile_projects_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    Global.selected_profile = self
    Global.set_panel(Global.homepage_content_panel, ViewProjects(item=self.item))
