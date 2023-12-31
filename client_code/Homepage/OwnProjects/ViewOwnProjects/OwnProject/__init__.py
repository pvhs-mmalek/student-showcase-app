from ._anvil_designer import OwnProjectTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...EditProject import EditProject
from ..... import Global
from .....ImageButton import ImageButton

class OwnProject(OwnProjectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if len(self.item['file_ids']) > 0:
      self.image_panel.clear()
      self.image_panel.add_component(ImageButton(item=self.item['file_ids']))
    else:
      self.image_panel.clear()
    
  def edit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    form = EditProject(item=self.item)
    Global.current_project = self.item
    Global.set_panel(Global.OwnProjects_content_panel, form)

  def delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('delete_project', self.item)
    Global.OwnProjects_repeating_panel.items = anvil.server.call('get_own_projects')
