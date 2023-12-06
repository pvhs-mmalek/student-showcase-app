from ._anvil_designer import EditProjectTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .... import Global
from ..ViewOwnProjects import ViewOwnProjects

class EditProject(EditProjectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    for image in self.item['images']:
      self.image_uploader.file += image

  def save_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    project = dict(self.item)
    project['title'] = self.title_box.text
    project['description'] = self.description_box.text
    project['images'] = self.image_uploader.files
    anvil.server.call('update_project', self.item, project)
    Global.set_panel(Global.OwnProjects_content_panel, ViewOwnProjects())
    

  def cancel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    Global.set_panel(Global.OwnProjects_content_panel, ViewOwnProjects())
