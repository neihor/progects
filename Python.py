from os import listdir
from os.path import isfile
from os.path import join as joinpath

mypath = "D:\python\papka1"
mysecondpath = "D:\python\papka2"
for i in listdir(mypath):
        print mypath + "\\" + i
import shutil
shutil.move(mypath, mysecondpath) 

