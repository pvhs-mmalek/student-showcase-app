from ._anvil_designer import EditProjectTemplate
from anvil import *
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
    

  def save_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    project = dict(self.item)
    project['title'] = self.title_box.text
    project['description'] = self.description_box.text
    Global.edited_image_list = anvil.server.call('get_own_projects', self.item)  
    Global.set_panel(self.edit_images_panel, RepeatingPanel(item_template=))
    self.edit_images_panel.clear()
    self.edit_images_panel.add_component(RepeatingPanel(item_template=EditOwnImages, items=Global.edited_image_list))

    print(self.image_uploader.file)
    anvil.server.call('update_project', self.item, project, images)
    Global.set_panel(Global.OwnProjects_content_panel, ViewOwnProjects())
    

  def cancel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    Global.set_panel(Global.OwnProjects_content_panel, ViewOwnProjects())
