from urllib.request import urlopen
link = 'https://s3.amazonaws.com/img.takeoff/manual/20180712-210211-e7b65c-4-99-232-874896005780.IMG9351.SNe7b65c.obj.0.1.jpg'
resource = urlopen(link)
name = link.split('/')
out = open(r'D:\DONE_PHOTOS_FROM_FREELANCERS\20181017_done_photos'+r'/'+name[5], 'wb')
out.write(resource.read())
out.close()
text = 'https://s3.amazonaws.com/img.takeoff/manual/20180712-210211-e7b65c-4-99-232-874896005780.IMG9351.SNe7b65c.obj.0.1.jpg'
a=text.split('/')
print(a[5])