from ._anvil_designer import UserProjectTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ....ImageButton import ImageButton

class UserProject(UserProjectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if len(self.item['file_ids']) > 0:
      self.image_panel.clear()
      self.image_panel.add_component(ImageButton(item=self.item['file_ids']))
    else:
      self.image_panel.clear()
