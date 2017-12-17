import sublime, sublime_plugin, os, sys, subprocess, threading

class GitBashHereCommand(sublime_plugin.WindowCommand):
  def run(self):
    settings = sublime.load_settings('GitBash Preferences.sublime-settings')
    gitbash_path = settings.get('gitbash_path')
    if not gitbash_path:
      print("The \"gitbash_path\" not set in GitBash Preferences.sublime-settings")
      return
    gitbash_parameters = settings.get('gitbash_parameters',[])
    if not isinstance(gitbash_parameters, list):
      print("The \"gitbash_parameters\" must be an array of strings")
      return
    view = self.window.active_view()
    if not view.file_name() or not os.path.dirname(view.file_name()):
      print('Can\'t run GitBash : missing folder.')
      return
    folder_name = os.path.dirname(view.file_name())
    print(u"Starting "+gitbash_path+" "+(" ".join(gitbash_parameters))+" in folder "+folder_name+" ...")
    # folder_name is unicode => system encoding ("mbcs" for windows)
    if (not (type(folder_name) is str)):
      folder_name = folder_name.encode(sys.getfilesystemencoding())
    subprocess.Popen(gitbash_path+" "+(" ".join(gitbash_parameters)), cwd=folder_name)
    # The following works only with gitbash_path="sh" :
    # self.window.run_command("exec", {"cmd": ["start", gitbash_path]+gitbash_parameters, "shell": True, "working_dir": folder_name})
    # self.window.run_command("hide_panel", {"panel": "output.exec"})
