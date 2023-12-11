from ._anvil_designer import ViewOwnProfileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ViewProfile import ViewProfile
from ..EditProfile import EditProfile
from ... import Global

class ViewOwnProfile(ViewOwnProfileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.content_panel.add_component(ViewProfile(item=self.item))

  def edit_profile_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    Global.set_panel(Global.homepage_content_panel, EditProfile(item=self.item))

