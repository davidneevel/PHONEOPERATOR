from random import randint
from time import sleep

while 1:
    i = randint(0,100)
    print ""
    print i
    if i < 25:
        print "< 25"
    elif i < 50:
        print "25 < i < 50"
    elif i < 75: 
        print "50 < i < 75"
    else:
        print "> 75"
    sleep(1)


    