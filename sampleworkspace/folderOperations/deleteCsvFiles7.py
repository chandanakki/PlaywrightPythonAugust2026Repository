#Case 6: In a List of 'N' Numbers Files Delete only .csv Files
import os
 
def delete_all_csv_files(folderpath):
    dirs=os.listdir(folderpath)
 
    for filename in dirs:
        full_path= folderpath + filename
        if(os.path.isfile(full_path)==True):
            if(full_path.endswith(".csv")):
                print(full_path)
                os.remove(full_path)
 
 
delete_all_csv_files("C:/Important Folder/PythonPlaywrightTrainingPgudi/Folders/")
