from ._anvil_designer import OwnProjectTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...EditProject import EditProject
from ..... import Global

class OwnProject(OwnProjectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if self.item['images'].length == 1:
      self.project_images.source = self.item['images'][0]
    elif self.item.length > 1:
      self.project_images.set_event_handler('click', self.image_click)

  def edit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    form = EditProject()
    form.item = self.item
    Global.set_panel(Global.OwnProjects_content_panel, form)

  def image_click(self, **event_args):
    images = self.item['images']
    index = images.index(self.project_images.source)
    if index+1 >= images.length:
      self.project_images.source = images[0]
    else:
      self.project_images.source = images[index+1]
    

