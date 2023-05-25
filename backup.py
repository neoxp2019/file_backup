#rev0001
import shutil
import os
import time

copy_from = 'C:\\1'
copy_to = 'C:\\2'
data_files= []
data_dirs= []
data_files_to= []
data_dirs_to= []
# ---
if os.path.isdir(copy_to) == True:
    shutil.rmtree(copy_to)
    time.sleep(1)
    os.mkdir(copy_to)
else:
    os.mkdir(copy_to)
# ---
for root, dirs, files in os.walk(copy_from):  
     for filename in files:
         data_files.append(root+"\\"+filename)
         data_files_to.append(root.replace('C:\\1','C:\\2')+"\\"+filename)
     for dir in dirs:
         data_dirs.append(root+"\\"+dir)
         data_dirs_to.append(root.replace('C:\\1','C:\\2')+"\\"+dir) 
# -----
for dir in data_dirs_to:
    os.mkdir(dir)
time.sleep(1)
#------
for i in range (0,len(data_files)-1):
    shutil.copy2(data_files[i], data_files_to[i])
