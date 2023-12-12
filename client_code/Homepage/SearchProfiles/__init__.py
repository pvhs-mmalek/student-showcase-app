from ._anvil_designer import SearchProfilesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .AdvancedSearch import AdvancedSearch

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

  def advanced_search_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    search_dict = {
      'min_gpa': 0,
      'min_gpa_check': False,
      'max_gpa': 5,
      'max_gpa_check': False,
      'min_act': 0,
      'min_act_check': False,
      'max_act': 36,
      'max_act_check': False,
      'min_sat': 0,
      'min_sat_check': False,
      'max_sat': 1600,
      'max_sat_check': False,
      'min_grade': 9,
      'min_grade_check': False,
      'max_grade': 12,
      'max_grade_check': False,
      'location': '',
      'location_check': False,
      'school': '',
      'school_check': False,
    }
    search_clicked = alert(
      content = AdvancedSearch(item=search_dict),
      title="Advanced Search",
      large = True,
      buttons = [('Cancel',False),('Search',True)],
      dismissible=False
    )
    if search_clicked:
      print(search_dict)
      temp = anvil.server.call('advanced_profile_search', search_dict)
      print(temp)
      self.repeating_profile_panel.items = temp


