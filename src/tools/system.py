import os
import subprocess
import sys

def open_file(file_path):
    """
    Opens a file in the default editor.
    """
    if sys.platform == "win32":
        os.startfile(file_path)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", file_path])
    else:
        subprocess.Popen(["xdg-open", file_path])
