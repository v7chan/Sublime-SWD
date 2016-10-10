import sublime
import sublime_plugin
import os
import ast

SETTINGS_FILE = "Preferences.sublime-settings"
DEFAULT = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.ttf', '*.tga', '*.dds', '*.ico', '*.eot', '*.pdf', '*.swf', '*.jar', '*.zip']
settings = None

class SetWorkingDirectoryCommand(sublime_plugin.TextCommand):
	def run(self, edit, paths):
		# current_ignore_paths = ast.literal_eval(settings.get('binary_file_patterns'))
		selected_folder = paths[0].split('/')[-1]
		
		all_folders = os.listdir(sublime.active_window().folders()[0])
		all_folders.remove(selected_folder)
		all_folders.remove('.DS_Store')
		
		ignore_folders = [folder + '/*' for folder in all_folders]
		new_ignore_list = DEFAULT + ignore_folders

		# print(settings.get('binary_file_patterns'))
		settings.set('binary_file_patterns', new_ignore_list)
		# print(settings.get('binary_file_patterns'))

class ClearWorkingDirectoryCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings.set('binary_file_patterns', DEFAULT)
		# print(settings.get('binary_file_patterns'))
	def is_enabled(self):
		return not settings.get('binary_file_patterns') == DEFAULT

def plugin_loaded():
	global settings
	settings = sublime.load_settings(SETTINGS_FILE)

	global DEFAULT
	DEFAULT = settings.get('binary_file_patterns')