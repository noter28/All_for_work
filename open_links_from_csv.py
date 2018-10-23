
# открываем все ссылки с csv файла
import webbrowser
import csv
from urllib.request import urlopen

with open('qwerty.csv') as f:
    reader = csv.reader(f)
    for link in reader:
        resource = urlopen(link[0])
        name = link[0].split('/')
        out = open(r'D:\DONE_PHOTOS_FROM_FREELANCERS\20181023_done_photos' + r'/' + name[7], 'wb')
        out.write(resource.read())
        out.close()
        text = name[7]
        a = text.split('/')
        print(text)
        # img = Image.open(directory + '\\' + (row[0]))
        # img.save(outcome_directory + '\\' + (row[0]))
        # os.remove(directory + '\\' + (row[0]))


            #cmd
            #
            # for char in line:
            #     if char in " ?.!/;:":
            #         line.replace(char, '')