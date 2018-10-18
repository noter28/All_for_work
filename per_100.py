# создание директории и перемещения туда файлов по 100 штук
import shutil
import os, sys
from PIL import Image #Python image library
just_photo =         r'D:\All_photos\20181013_photo' #first source
redo_directory = (r'D:\All_photos\20181013_unzip\redo_20181010_01__213')     #output manually cropping photo
def create_redo_directory():
    files = os.listdir(just_photo) #list of item in directory
    a=0
    b = os.makedirs(redo_directory)
    for i  in files:
        shutil.move(just_photo + '\\' + i, redo_directory)
        a+=1
        print(a)
        if a>=210:
            break
create_redo_directory()