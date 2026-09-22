#Case 6: File Collections, It should display only the Files.
 
import os
def file_collections_demo(folderpath):
    dirs=os.listdir(folderpath)
 
    for filename in dirs:
        full_path=folderpath + filename
 
        if(os.path.isfile(full_path)==True):
            print(full_path)
 
 
 
file_collections_demo("C:/Important Folder/PythonPlaywrightTrainingPgudi/Folders/")