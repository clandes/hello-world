import shutil
from os import listdir
from os.path import isfile, join

DIR_A = "C:\\Users\\Cheryl\\Desktop\\Customers"
DIR_B = "C:\\Users\\Cheryl\\Desktop\\CustomerDailyUpdates"

onlyfiles_A = [ f for f in listdir(DIR_A) if isfile(join(DIR_A,f)) ]
onlyfiles_B = [ f for f in listdir(DIR_B) if isfile(join(DIR_B,f)) ]

for f_a in onlyfiles_A:
    if not f_a in onlyfiles_B:
        src = DIR_A+"/"+f_a
        shutil.copy(src, DIR_B)
