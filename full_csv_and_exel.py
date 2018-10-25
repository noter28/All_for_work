import csv
import os, sys
import shutil
from PIL import Image
directory =         r'D:\All_photos\20181019_photo' #first source
outcome_directory = (r'D:\\All_photos\20181019_done_photos_for_redone')
with open('list_20180831_for_download.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            shutil.move(directory + '\\' + (row[0]), outcome_directory)
        except FileNotFoundError:
            print(row[0])
        # finally:
        #     print(row[0])
        #     shutil.move(directory + '\\' + (row[0]), outcome_directory)
        #     a+=1
        #     print(a)
        #     if a>=100:
        #         c
        #         b
        #         print(a)
        #         a == 002
