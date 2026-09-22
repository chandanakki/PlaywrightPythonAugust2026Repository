#Case 5: Remove Multiple Existing Folders or Directories
import os
 
def remove_multiple_folders(folderpath):
    os.removedirs(folderpath)
 
remove_multiple_folders("C:/Important Folder/PythonPlaywrightTrainingPgudi/Folders/A/B/C/D/E/F/G")