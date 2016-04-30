#!/usr/bin/env python
import os
from os import listdir, mkdir, rmdir
from os.path import isfile, join, isdir,getmtime, getctime
import time
import sys
import pyexiv2
from shutil import copy

path = sys.argv[1]
print ("path = "+path)
list_of_files_and_folders = listdir(path)
#temp_path = join(path,"temp")
temp_path = join("/home/tiphanie", "temp")
errors = []

mkdir(temp_path)
print("temp_path = "+temp_path)

def move_file(file=''):
        print("file to handle = "+file)
        try:
            metadata = pyexiv2.ImageMetadata(file) 
            metadata.read()
            #print(metadata.exif_keys)
            tag = metadata['Exif.Image.DateTime']
            mydate = tag.raw_value
            mydate = tag.value.strftime('%d'+'_'+'%B'+'_'+'%Y')
            #print("my date = "+mydate)
            new_path=join(temp_path,mydate)
            #print("new path = "+new_path)
            if isdir(new_path):
                #print ("there is already one, we just add the picture")
                pass
            else:
                #print("folder not yet exists, let's create it")
                mkdir(new_path)
            copy(file,new_path)
        except:
            errors.append(file)

for root, directories, filenames in os.walk(path):
    for filename in filenames:
        move_file(join(root,filename))

if len(errors) > 0:
    print('Files with error: ')
    print(errors)
