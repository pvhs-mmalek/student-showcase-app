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
from ..ViewProfile import ViewProfile

class EditProfile(EditProfileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if self.item['profile_image'] != None:
      self.profile_image.source = anvil.server.call('get_image', self.item['profile_image'])
    if self.item['project_image'] != None:
      self.project_image.source = anvil.server.call('get_image', self.item['project_image'])
    
  
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
    profile_dict['act'] = self.act_box.text
    profile_dict['sat'] = self.sat_box.text
    profile_dict['about'] = self.about_box.text
    profile_dict['project_title'] = self.title_box.text
    profile_dict['project_desc'] = self.project_description.text
    profile_dict['profile_image'] = self.item['profile_image']
    profile_dict['project_image'] = self.item['project_image']
    anvil.server.call('update_profile', self.item, profile_dict)
    self.item = anvil.server.call('get_own_profile')
    Global.set_panel(Global.homepage_content_panel, ViewProfile(item=self.item))

  def profile_image_load_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if self.item['profile_image'] != None:
      anvil.server.call('delete_image', self.item['profile_image'])
    image_id = anvil.server.call('add_image_return_id', file)
    anvil.server.call('set_profile_image_id', self.item, image_id)
    self.profile_image.source = anvil.server.call('get_image',image_id)

  def project_image_load_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if self.project_image == None:
      anvil.server.call('delete_image', self.item['project_image'])
    image_id = anvil.server.call('add_image_return_id', file)
    anvil.server.call('set_profile_project_image_id', self.item, image_id)
    self.project_image.source = anvil.server.call('get_image',image_id)


