import shutil
import os, sys
import zipfile
from funcs import write_result
directory =         os.path.join('D:/','DONE_PHOTOS_FROM_FREELANCERS','20181205_links_for_upload') #first source
outcome_directory = directory + r'_unzip'     #output manually cropping photo
just_photo = directory + r'_photo'
files = os.listdir(directory) #list of item in directory
for i in files:
    s=i.replace('.','-')
    s=s.split('-')
    a=(s[6])
    while len(a)!=14:
        a='0'+a
    l='https://s3.amazonaws.com/img.takeoff/manual/'+i
    text=a+','+l+','+i+','+s[6]+'\n'
    write_result('for_upload.csv', text)