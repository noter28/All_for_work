import webbrowser
import csv
from urllib.request import urlopen
from funcs import write_result

'''
def write_result(output_doc_name, text):
    with open(output_doc_name, "a") as file:
        file.write(text)
'''
with open('images.csv') as f:
    reader = csv.reader(f)
    for link in reader:
        try:
            resource = urlopen(link[0])
            name = link[0].split('/')
            out = open(r'D:\DONE_PHOTOS_FROM_FREELANCERS\transformer' + r'/' + name[7], 'wb')
            out.write(resource.read())
            out.close()
        except Exception:
            write_result('errors.csv', (link[0] + '\n'))
            print(link)
            pass
