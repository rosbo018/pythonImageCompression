#!/usr/bin/python
 
import subprocess
import sys
from PIL import Image
 
path = sys.argv[1]
files  = subprocess.check_output(["ls", path])
files = str(files)
fileSplit = files.split("\n")
jpg = []
for x in fileSplit:
    if (".jpg" in x or ".png" in x):
        jpg.append(x)
 
for x in jpg:
    imagePath = path + "//" + x
    print imagePath
    foo = Image.open(imagePath)
    foo = foo.resize((foo.size[0], foo.size[1]), Image.ANTIALIAS)
    fileExtension = x[-4:]
    fileName = x[:-4]
    print fileExtension
    downgradePath = path + "//" + fileName + "_downgrade.jpg"
    print imagePath+ fileName+downgradePath
    if(fileExtension == ".jpg"):
        foo.save(downgradePath, "JPEG", quality=1)
        foo.close()
    else:
        jpgConvert = foo.convert('RGB')
        jpgConvert.save(downgradePath, "JPEG", quality=1)
        foo.close()
