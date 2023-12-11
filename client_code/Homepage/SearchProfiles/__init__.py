from ._anvil_designer import SearchProfilesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SearchProfiles(SearchProfilesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if self.item:
      self.search_box.text = self.item
      self.repeating_profile_panel.items = anvil.server.call('search_profiles_by_name', self.search_box.text)
    else:
      self.repeating_profile_panel.items = anvil.server.call('search_profiles_by_name', False)

  def search_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.repeating_profile_panel.items = anvil.server.call('search_profiles_by_name', self.search_box.text)


