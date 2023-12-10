from ._anvil_designer import ImageButtonTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Global

class ImageButton(ImageButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.images = anvil.server.call('get_images', self.item)
    self.project_image.source = self.images[self.index]
    check_image_buttons(self)

  def prev_image_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.index -= 1
    check_image_buttons(self)
    self.project_image.source = self.images[self.index]

  def next_image_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.index += 1
    check_image_buttons(self)
    self.project_image.source = self.images[self.index]
    
def check_image_buttons(self, **event_args):
  if self.index < 1:
    self.prev_image_button.enabled = False
    self.prev_image_button.visible = False
  else:
    self.prev_image_button.enabled = True
    self.prev_image_button.visible = True
  if self.index == len(self.item)-1:
    self.next_image_button.enabled = False
    self.next_image_button.visible = False
  else:
    self.next_image_button.enabled = True
    self.next_image_button.visible = True
  
