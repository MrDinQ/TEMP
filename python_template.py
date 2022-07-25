# ---------------------------------------------------------------------------------------- #
#                               TEMPLATE                                                   #
# ---------------------------------------------------------------------------------------- #
import os
import sys
import re
import tempfile

# GENERAL INFO
template_folder = '1my_2anchor_3_template.txt'
template_data_folder = '1my_2_data_3folder_template.txt'
# Get default working directory and other info
try:
    current_working_directory = os.getcwd()
    current_file_directory = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_file_directory)
    other_files_in_current_directory = os.listdir()
    current_file_name = os.path.basename(__file__)
except:
    try:
        current_working_directory = os.getcwd()
        current_file_directory = os.path.dirname(os.path.realpath('__file__'))
        os.chdir(current_file_directory)
        other_files_in_current_directory = os.listdir()
        current_file_name = os.path.basename('__file__')
    except:
        try:
            current_working_directory = tempfile.gettempdir()
            current_file_directory = tempfile.gettempdir()
            os.chdir(tempfile.gettempdir())
            other_files_in_current_directory = os.listdir()
            current_file_name = os.path.basename('file')
        except:
            print('DIR and FILE ISSUE')              

# UPDATE PIP
try:
    if sys.platform == "win32":
        os.system(f'python -m pip install --upgrade pip')
    elif sys.platform == "darwin":
        os.system(f'python3 -m pip install --upgrade pip')
    elif sys.platform == "linux":
        os.system(f'sudo apt update')
        os.system(f'sudo apt install python3-pip')
        os.system(f'python3 -m pip install --upgrade pip')
    else:
        pass
except:
    pass

# BETTER IMPORT
def import_or_install(package):
    try:
        # if importlib is not available then install it
        try:
            __import__('importlib')
        except:
            if sys.platform == "win32":
                os.system(f'python -m pip install importlib')
            elif sys.platform == "darwin":
                os.system(f'python3 -m pip install importlib')
            elif sys.platform == "linux":
                os.system(f'python3 -m pip install importlib')
            else:
                pass
            # import importlib
            import importlib

        # if module in .py not found then pip install it
        try:
            current_file_directory_func = os.path.dirname(os.path.realpath('__file__'))
            result = []
            py_package = str(package+'.py')

            for root, dir, files in os.walk(current_file_directory_func):  # Walking top-down from the root
                if py_package in files:
                    result.append(os.path.join(root, py_package))

            if len(result) == 0:
                try:
                    __import__(package)
                except:
                    if sys.platform == "win32":
                        os.system(f'python -m pip install {package} > nul')
                    elif sys.platform == "darwin":
                        os.system(f'python3 -m pip install {package}')
                    elif sys.platform == "linux":
                        os.system(f'python3 -m pip install {package}')
                    else:
                        print('not known OS')
            else:
                sys.path.append(result[0].replace(py_package, ''))
        except:
            print(str(package)+' not installed')    
    except:
        print(str(package)+' not installed')




# Get folder hierachy
try:
    folder_hierachy = current_file_directory.split('\\')
    if len(folder_hierachy) == 0:
        folder_hierachy = current_file_directory.split('/')
    else:
        folder_hierachy

    # root folder
    if sys.platform == "win32":
        root_folder = f'{folder_hierachy[0]}\\'
    else:
        root_folder = f'{folder_hierachy[0]}/'
        print(root_folder) 

    # Upper one folder
    fi = 1
    upper_folder = f'{root_folder}'
    while fi < len(folder_hierachy)-1:
        if sys.platform == "win32":
            upper_folder = f'{upper_folder}'+ f'{folder_hierachy[fi]}\\'
            fi +=1
        else:
            upper_folder = f'{root_folder}'
            upper_folder = f'{upper_folder}'+ f'{folder_hierachy[fi]}\\'
            fi +=1
except:
    pass
# Import Customized module & re-set working directory
try:
    import_or_install('module_find_files');  from module_find_files import *
    this_app_folder = re.sub(template_folder,'',module_find_files.find_files(template_folder, upper_folder))
    this_app_data_folder = re.sub(template_data_folder,'',module_find_files.find_files(template_data_folder, upper_folder))
    os.chdir(this_app_data_folder)
    print("\n \nCURRENT WORKING DIRECTORY: ",os.getcwd())
    print("\n \nCURRENT APP DATA FOLDER: ",this_app_data_folder)
    print("\n \nCURRENT APP DIRECTORY: ", this_app_folder)
    print("\n \n")
except:
    pass
# OTHER VARIALBES
# upper_folder; current_file_name; folder_hierachy; os.listdir(); root_folder



# OPTIONAL - READ DATA
'''
import_or_install('pandas'); import pandas as pd
import_or_install('pandasql'); import pandasql as ps

personal_data_path = module_find_files.find_files('Personal_Data.xlsx',my_directory)
personal_data_df = pd.read_excel(personal_data_path,sheet_name='Memo')
'''

# OPTIONAL - INPUT WINDOW
# import tkinter as tk
# from tkinter import simpledialog
'''
ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:")
tk.messagebox.showinfo(title=None, message=USER_INP)
'''
import_or_install('os')
print(current_file_directory)
print(current_file_name)

# ---------------------------------------------------------------------------------------- #
#                                   MAIN CODE                                              #
# ---------------------------------------------------------------------------------------- #


