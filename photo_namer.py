
import os
import sys
import shutil


directory = "./test"

x = 0
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file = directory + "/" +filename
       	fileNew = directory + "/newName" + str(x) + ".txt"

       	os.rename(file, fileNew)
        print(fileNew)
        
    else:
        continue
    x += 1
