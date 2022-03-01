from datetime import datetime


now = datetime.now()
current_time = now.strftime("%d:%m:%y - %H:%M:%S\n")

f = open('file2.txt',"a")
f.write(f'{current_time}')
f.close()