# Inspiration taken from https://github.com/wesf90/rails-partial
# Thanks!

import os
import sublime, sublime_plugin

class TextmasterFrameworkCommand(sublime_plugin.TextCommand):
  root_path    = ""
  module_path_list = None

  def run(self, edit):
    self.edit            = edit
    self.view.window().show_input_panel("New Controller and View Path (ex: client_area/index )", "", self.trigger, None, None)

  def trigger(self, user_entry):
    base_path = os.path.dirname(self.view.file_name())

    os.chdir(base_path)
    self.root_path = self.find_root_path(base_path, 0)

    formatted_entry = user_entry.encode('utf-8')

    if formatted_entry.split('/')[0] == '':
      self.module_path_list = user_entry.split('/')[1:]
    else:
      self.module_path_list = user_entry.split('/')

    os.chdir(self.js_pages_path())
    self.create_js_module_arbo(self.module_path_list)
    self.display_message("Success")

  def create_js_module_arbo(self, list):
    if not list:
      #create framework files
      self.create_files()
    else:
      dir_name = list[0]
      if not os.path.isdir(dir_name): os.makedirs(dir_name)
      os.chdir(dir_name)
      self.create_js_module_arbo(list[1:])

  def create_files(self):
    controller_path = os.path.join(os.getcwd() , "controller.coffee")
    view_path       = os.path.join(os.getcwd() , "view.coffee")
    base_coffee     = os.path.join(self.js_src_path(), "base.coffee")

    if os.path.isfile(controller_path):
      #file exists
      self.display_message("Controller already exists")
      return
    else:
      with open(controller_path, 'w') as f:
        f.write(self.base_controller_content())

    if os.path.isfile(view_path):
      #file exists
      self.display_message("View already exists")
      return
    else:
      with open(view_path, 'w') as f:
        f.write(self.base_view_content())

    initial_window = self.view.window()
    base_view = initial_window.open_file(base_coffee,     1)
    initial_window.open_file(controller_path, 1)
    initial_window.open_file(view_path,       1)

    initial_window.focus_view(base_view)


  def find_root_path(self, path, index):
    #convention: root_path contains Gemfile
    #avoid infinite recursion
    if index == 20:
      # self.display_message("Unable to find root path")
      return

    if os.path.isfile(os.path.join(path ,"Gemfile")):
      return path
    else:
      os.chdir('..')
      return self.find_root_path(os.getcwd(), index + 1)

  def base_controller_content(self):
    return """#= require './view'
module = """ + self.camelized_module_name() + """

class module.Controller extends Framework.Controller
  @options {
    View: module.View
      events:
        'event_name': { el: 'elt_name', type: 'click' }
  }"""

  def base_view_content(self):
    return """module = """ + self.camelized_module_name() + """
    
class module.View extends Framework.View
  @options {
    selectors:
      your_selector:
  }"""

  def camelized_module_name(self):
    camelized_list = [self.lower_case_underscore_to_camel_case(name) for name in self.module_path_list]
    return "Textmaster." + ".".join(camelized_list)

  def lower_case_underscore_to_camel_case(self, string):
    class_ = string.__class__
    return str.join('.', map(class_.capitalize, string.split('_')))

  def js_src_path(self):
    return os.path.join(self.root_path, "app", "assets", "javascripts", "src")

  def js_pages_path(self):
    return os.path.join(self.js_src_path(), "pages")

  def display_message(self, value):
    sublime.active_window().active_view().set_status("textmaster_framework_msg", value)



