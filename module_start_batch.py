import os
import sys
import subprocess

class module_start_batch:
    def __init__(self,file):
        self.file = file

    def start_batch(file): 
        file = file
        if sys.platform == "win32":
            os.startfile(file)
        elif sys.platform == "darwin":
            opener = "open"
            subprocess.call([opener, file])
        elif sys.platform == "linux":
            opener = "open"
            subprocess.call(['xdg-open', file])
        else:
            pass

print('module_start_batch.start_batch(file_path)')
