import os
import shutil

source = input("please enter a sourcefolder name:")
dest = input("Please enter your destination folder:")

source = source + '/'
dest = dest +'/'

files = os.listdir(source)

#print(source)
#print(files)
#print(dest)

for file in files:
    shutil.copy(source + file,dest)
    print(source+file)


