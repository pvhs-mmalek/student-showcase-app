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

  def edit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    form = EditProject()
    form.item = self.item
    Global.set_panel(Global.OwnProjects_content_panel, form)

