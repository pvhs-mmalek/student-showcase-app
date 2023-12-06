from ._anvil_designer import ImageButtonTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ImageButton(ImageButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.image_list = anvil.server.call('test_get_image')
    # for img in self.item:
    #   self.image_list += [img['image']]
    self.image = self.image_list[self.index]['image']
    print(self.index)
    print(self.image)
    print(self.image_list)
    if self.index > 0:
      self.prev_image_button.visible = True
      self.prev_image_button.enabled = True
    else:
      self.prev_image_button.visible = False
      self.prev_image_button.enabled = False
    if self.index == len(self.image_list):
      self.next_image_button.visible = True
      self.next_image_button.enabled = True
    else:
      self.next_image_button.visible = False
      self.next_image_button.enabled = False

  def prev_image_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.index-=1
    self.project_image.source = self.image_list[self.index]
    self.refresh_data_bindings()

  def next_image_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.index+=1
    self.project_image.source = self.image_list[self.index]
    self.refresh_data_bindings()

  
