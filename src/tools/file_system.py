# File System Tools
import os

def read_file(file_path):
    """
    Read the content of a file.
    """
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path, content):
    """
    Write content to a file.
    """
    with open(file_path, 'w') as f:
        f.write(content)

def list_directory(path):
    """
    List the files and directories in a path.
    """
    return os.listdir(path)
