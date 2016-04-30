#!/usr/bin/env python
from os import listdir, mkdir, rmdir
from os.path import isfile, join, isdir,getmtime, getctime
import time
import sys
import pyexiv2
from shutil import copy

path = sys.argv[1]
print ("path = "+path)
list_of_files_and_folders = listdir(path)
list_of_files = []
temp_path = join(path,"temp")

mkdir(temp_path)
print("temp_path = "+temp_path)

for elem in list_of_files_and_folders:
    file = join(path,elem)
    if isfile(file):
        metadata = pyexiv2.ImageMetadata(file) 
        metadata.read()
        metadata.exif_keys
        tag = metadata['Exif.Image.DateTime']
        mydate = tag.raw_value
        mydate = tag.value.strftime('%A'+'_'+'%d'+'_'+'%B'+'_'+'%Y')
        print("my date = "+mydate)
        new_path=join(temp_path,mydate)
        print("new path = "+new_path)
        if isdir(new_path):
            print ("there is already one, we just add the picture")
            pass
        else:
            print("folder not yet exists, let's create it")
            mkdir(new_path)
        copy(file,new_path)

        #print ("date = "+mydate[0:10])
        #print ("date = "+tag.value.strftime('%A %d %B %Y, %H:%M:%S'))
        #print ("date = "+tag.value.strftime('%A'+'_'+'%d'+'_'+'%B'+'_'+'%Y'))
        



