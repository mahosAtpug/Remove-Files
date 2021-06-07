import os
import shutil
import time

def code():

    deletedFolderCount = 0
    deletedFileCount = 0
    path = "./try"
    days = 0
    seconds = time.time() - (days * 24 * 60 *60)

    if os.path.exists(path):
        for root_folder , folders , files in os.walk(path):
            if seconds>= getFileOrFolderAge(path):
                remove_folder(root_folder)
                deletedFolderCount +=  1

                break

            else:
                for folder in folders:
                    folderPath = os.path.join(root_folder , folder)
                    if seconds >= getFileOrFolderAge(folderPath):
                        remove_folder(folderPath)
                        deletedFolderCount += 1

                for file in files:
                    filePath = os.path.join(root_folder , file)
                    if seconds >= getFileOrFolderAge(filePath):
                        remove_file(filePath)
                        deletedFileCount += 1  
                
    else:
        print("Path Not Found")

    print("Number Of Files Deleted :"  , deletedFileCount)
    print("Number Of Folders Deleted :"  , deletedFolderCount)

def remove_file(path):
    if not os.remove(path):
        print("File removed Succesfully")

    else:
        print("Unable To Remove The File")

def remove_folder(path):
    if not shutil.rmtree(path):
        print("Folder Removed Succesfully")

    else:
        print("Unable to Remove Folder")

def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime


code()



    

            





    


