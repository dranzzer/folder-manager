import os
import shutil
folder_path = 'C:/Users/Tharindu/Documents/folder-manager/New folder'
os.chdir(folder_path)
for file in os.listdir(folder_path):
    file_name = os.path.splitext(file)[0]
    final_path = folder_path + '/' + file_name + '/'

    os.mkdir(final_path)
    shutil.copy(file, final_path)