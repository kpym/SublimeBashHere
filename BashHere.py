import sublime, sublime_plugin, os, sys, subprocess, threading

class BashHereCommand(sublime_plugin.WindowCommand):
  def run(self, path = None, parameters = []):
    if path is None:
      print("No 'path' parameter passed as argument to the command 'bash_here'.")
      return
    if not isinstance(parameters, list):
      print("The \"parameters\" must be an array of strings")
      return
    view = self.window.active_view()
    if not view.file_name() or not os.path.dirname(view.file_name()):
      print('Can\'t run BashHere : missing folder.')
      return
    folder_name = os.path.dirname(view.file_name())
    print(u"Starting "+path+" "+(" ".join(parameters))+" in folder "+folder_name+" ...")
    # folder_name is unicode => system encoding ("mbcs" for windows)
    if (not (type(folder_name) is str)):
      folder_name = folder_name.encode(sys.getfilesystemencoding())
    subprocess.Popen(path+" "+(" ".join(parameters)), cwd=folder_name)
    # The following works only with path="sh" :
    # self.window.run_command("exec", {"cmd": ["start", path]+parameters, "shell": True, "working_dir": folder_name})
    # self.window.run_command("hide_panel", {"panel": "output.exec"})
