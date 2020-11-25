
import os
import sys
import shutil
from PIL import Image

directory = "./2019/07"

x = 0
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        file = directory + "/" +filename
        try:
        	img = Image.open(file).getexif()[36867]
        	fileNew = directory + "/" + img[5:7] + "_" + img[8:10] + "_" + img[0:4] + "___" + str(x) + ".jpg"
       		print(fileNew)

       		os.rename(file, fileNew)

       	except :
       		pass

        #print(fileNew)
    x += 1
