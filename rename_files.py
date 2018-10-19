
import os, sys
from PIL import Image #Python image library

directory =         r'D:\\DONE_PHOTOS_FROM_FREELANCERS\20181019_done_photos\done_Dropbox\6.5_uah' #first source
outcome_directory = r'C:\\Users\descpc\Desktop\outcome_IC'     #output manually cropping photo
files = os.listdir(directory) #list of item in directory
for i  in files:
    img = Image.open(directory + '\\' + i)
    img.save(outcome_directory + r'another' + (i))