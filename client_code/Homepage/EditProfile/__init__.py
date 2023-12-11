from ._anvil_designer import EditProfileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Global

class EditProfile(EditProfileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def cancel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    Global.set_panel(Global.homepage_content_panel, Global.own_profile)

  def save_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    profile_dict = dict(self.item)
    profile_dict['name'] = self.name_box.text
    profile_dict['age'] = self.age_box.text
    profile_dict['sex'] = self.sex_dropdown.selected_value
    profile_dict['location'] = self.location_box.text
    profile_dict['school'] = self.school_box.text
    profile_dict['grade'] = self.grade_box.text
    profile_dict['gpa'] = self.gpa_box.text
    if self.act_check_box.checked:
      profile_dict['act'] = self.act_box.text
    if self.sat_check_box.checked:
      profile_dict['sat'] = self.sat_box.text
    profile_dict['about'] = self.about_box.text
    profile_dict['project_title'] = self.title_box.text
    profile_dict['project_desc'] = self.project_description.text
    anvil.server.call('update_profile', self.item, profile_dict)
    Global.own_profile.item = self.item
    Global.set_panel(Global.homepage_content_panel, Global.own_profile)

  def profile_image_load_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    anvil.server.call('delete_image', self.item['profile_image'])
    self.item['profile_image'] = anvil.server.call('add_image_return_id', file)

  def project_image_load_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass


