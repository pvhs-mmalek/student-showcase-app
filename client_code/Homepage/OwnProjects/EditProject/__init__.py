from ._anvil_designer import EditProjectTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .... import Global
from ..ViewOwnProjects import ViewOwnProjects
from .EditOwnImages import EditOwnImages

class EditProject(EditProjectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    Global.current_project = self.item
    Global.edit_image_panel = self.edit_images_panel
    self.edit_images_panel.clear()
    if len(self.item['file_ids']) > 0:
      self.edit_images_panel.add_component(RepeatingPanel(item_template=EditOwnImages, items=self.item['file_ids']))
    

  def save_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    project = dict(self.item)
    project['title'] = self.title_box.text
    project['description'] = self.description_box.text
    anvil.server.call('update_project', self.item, project)
    
    Global.set_panel(Global.OwnProjects_content_panel, ViewOwnProjects())
    

  def cancel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    Global.set_panel(Global.OwnProjects_content_panel, ViewOwnProjects())

  def image_uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    anvil.server.call('add_project_image', self.item, file)
    Global.set_panel(self.edit_images_panel, RepeatingPanel(item_template=EditOwnImages, items=self.item['file_ids']))
