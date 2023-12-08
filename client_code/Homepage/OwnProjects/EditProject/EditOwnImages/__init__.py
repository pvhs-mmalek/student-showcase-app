from ._anvil_designer import EditOwnImagesTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..... import Global

class EditOwnImages(EditOwnImagesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.project_image.source = self.item

  def change_project_image_button_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.item = self.change_project_image_button.file
    self.project_image.source = self.item

  def delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    Global.edited_image_list.remove(self.item)
    Global.set_panel(Global.edit_image_panel, Global.edited_image_list)
    
    
