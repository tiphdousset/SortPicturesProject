#!/usr/bin/env python
import os
from os import listdir, mkdir, rmdir
from os.path import isfile, join, isdir,getmtime, getctime
import time
import sys
import pyexiv2
from shutil import copy, rmtree
import exiftool

path = sys.argv[1]
print ("path = "+path)
list_of_files_and_folders = listdir(path)
temp_path = join("/home/tiphanie", "temp")
errors = []

try:
    mkdir(temp_path)
    print("temp_path = "+temp_path)
except:
    print("temp_path already exists")
    rmtree(temp_path)
    mkdir(temp_path)
    print("temp_path is now empty")

def move_file(file=''):
        print("file to handle = "+file)
        try:
            with exiftool.ExifTool() as et:
                metadata = et.get_metadata(file)
            print(metadata)
            print("\n")
            with exiftool.ExifTool() as et:
                #picture case
                tag = et.get_tag("EXIF:DateTimeOriginal",file)
                if tag == None:
                    #video case
                    tag = et.get_tag("QuickTime:CreateDate",file)
            print("tag")
            print(tag)
            print("\n")
            if tag == None:
                mydate = "other"
            else:
                mydate = tag[:10].replace(":","-")
            print("my date = "+mydate)
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
            print("Data info not found")
 
for root, directories, filenames in os.walk(path):
    for filename in filenames:
        move_file(join(root,filename))

if len(errors) > 0:
    pass
    #print('Files with error: ')
    #print(errors)
