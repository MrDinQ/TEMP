class module_find_files:
    import os
    import sys


    def __init__(self,filename, search_path):
        self.filename = filename
        self.search_path = search_path


    def find_files(filename = 'module_find_files', search_path = os.path.dirname(os.path.realpath('__file__'))):


        # ---------------------------------------------------------------------------------------- #
        #                               TEMPLATE                                                   #
        # ---------------------------------------------------------------------------------------- #
        import os
        import sys
        current_file_directory = os.path.dirname(os.path.realpath("__file__"))  # Current file's directory
        current_file_name = os.path.basename("__file__")  # Current file's name
        # print("Current directory: ", current_file_directory, "\n")
        # print("Current file's name: ",current_file_name, "\n")


        def import_or_install(package):

            try:
                __import__('importlib')
            except ImportError:
                if sys.platform == "win32":
                    os.system(f'python -m pip install importlib')
                elif sys.platform == "darwin":
                    os.system(f'python3 -m pip install importlib')
                else:
                    pass
            import importlib
            
            # current_file_directory_func = os.path.dirname(os.path.realpath('__file__'))
            current_file_directory_func = "C:\\Users\\hoa.dinh\\OneDrive - JLL\\TASKS\\Programming\\Projects\\APP_TKinter_Matplot_API"
            result = []
            py_package = str(package+'.py')

            for root, dir, files in os.walk(current_file_directory_func):  # Walking top-down from the root
                if py_package in files:
                    result.append(os.path.join(root, py_package))

            if len(result) == 0:
                try:
                    __import__(package)
                except ImportError:
                    if sys.platform == "win32":
                        os.system(f'python -m pip install {package}')
                    elif sys.platform == "darwin":
                        os.system(f'python3 -m pip install {package}')
                    else:
                        pass
            else:
                sys.path.append(result[0].replace(py_package, ''))





        # ---------------------------------------------------------------------------------------- #
        #                                   MAIN CODE                                              #
        # ---------------------------------------------------------------------------------------- #
        import_or_install('Pathlib'); from pathlib import Path
        result = []
        for root, dir, files in os.walk(search_path):  # Walking top-down from the root
            if filename in str(files) and len(result) == 0 and 'Windows\Recent' not in root:
                result.append(os.path.join(root, filename))
                print(f'FOUND HERE: {os.path.join(root, filename)}')
            else:
                pass
        print(f'ONLY FIRST VALUE IS RETURNED: {result[0]}')
        return str(Path(result[0]))  # Returns path of first found file
        

    def confirmation():
        print("Imported: module_find_files.find_files(file,search_path). This module returns str(Path(first_file_found)) \n")

module_find_files.confirmation()
