# import re
# result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
# print(result.group(0))
# def qwe(x,b,c):
#     q=x*b
#     return q
# def wer():
#     p=qwe(10,10,10)+2
#     return (p)
# print(wer())
# открываем все ссылки с csv файла
import webbrowser
import csv

with open('qwerty.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        webbrowser.open(row[0], new=0, autoraise=True)
        # img = Image.open(directory + '\\' + (row[0]))
        # img.save(outcome_directory + '\\' + (row[0]))
        # os.remove(directory + '\\' + (row[0]))


            #
            #
            # for char in line:
            #     if char in " ?.!/;:":
            #         line.replace(char, '')