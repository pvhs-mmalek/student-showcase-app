from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from .. import Global
from .OwnProjects import OwnProjects
from .ViewOwnProfile import ViewOwnProfile
from .SearchProfiles import SearchProfiles

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()
    anvil.server.call('check_new_user')
    Global.homepage_content_panel = self.content_panel
    self.search_profiles_button.raise_event('click')
    
    

  def logout_button_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.logout()
    anvil.users.login_with_form()
    anvil.server.call('check_new_user')

  def own_projects_button_click(self, **event_args):
    """This method is called when the link is clicked"""
    form = OwnProjects()
    self.content_panel.clear()
    self.content_panel.add_component(form)

  def view_own_profile_button_click(self, **event_args):
    """This method is called when the link is clicked"""
    Global.own_profile = ViewOwnProfile(item=anvil.server.call('get_own_profile'))
    self.content_panel.clear()
    self.content_panel.add_component(Global.own_profile)

  def search_profiles_button_click(self, **event_args):
    """This method is called when the link is clicked"""
    form = SearchProfiles()
    self.content_panel.clear()
    self.content_panel.add_component(form)

 