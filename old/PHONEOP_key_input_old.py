import smbus   

import time
from time import sleep
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

moveY = 1
moveX = 2
servoUp = 3
servoDown = 4
servoTap = 5
servoTo = 6
zero = 7
xy = 8


# This is the address we setup in the Arduino Program
ard1 = 0x04
var = 0

def checkStatus():  # checks and waits until not busy
    gettingStatus = 1;
    while gettingStatus == 1:
        try:
            status = bus.read_byte(ard1)
            if status == 100:    # 100 means ready
                print "ard1 ready"
                gettingStatus = 0
            else:
                print "ard1 busy"
                sleep(1)
        except:
            print "ard1 is offline. trying again"
            sleep(1)




def y(value): # waits until ard isn't busy then moves
    checkStatus()
    b = int(round(value/100))
    # print "b = %d" % b
    c = value - (b * 100)
    # print "c = %d" %c
    bus.write_i2c_block_data(ard1,1,[b,c,0,0])
    sleep(.1)

def x(value):
    checkStatus()   # is arduino busy?
    b = int(round(value/100))
    c = value - (b * 100)
    bus.write_i2c_block_data(ard1, moveX,[b,c,0,0])
    sleep(.1)

def servo(value):
    checkStatus()
    bus.write_i2c_block_data(ard1, servoTo,[0,value,0,0])
    print servoTo
    print 0
    print value
    sleep(.1)

def zero():
    checkStatus()
    bus.write_i2c_block_data(ard1, 7,[0,0,0,0])

def tap():
    checkStatus()
    bus.write_i2c_block_data(ard1, servoTap, [0,0,0,0])

# STARTING

# #check on arduino 1
status1 = 0

checkStatus()



# arduinos are online! available to be moved 


while True:
    try:
        var = int(raw_input("move y to:"))
        if var == 0:
            zero()
            print 'zero'

        y(var)
    except ValueError:
        print "OK not moving Y"
        # continue 

    

    try: 
        var = int(raw_input("move x to:"))
        x(var)
    except ValueError:
        print "OK not moving X"
        # continue
    
   

    try: 
        a = raw_input("move servo to:")
        var = int(a)
        servo(var)
    except ValueError:
        print "OK not moving servo"
        if a == "t":
            print "tappy"
            tap()
        continue
    
    





#bus.write_i2c_block_data(ard1, 1, [2, 00] )



# bus.write_byte(ard1, 1)   # means it's going to move up
# while status1 != 1:
#     print "waiting for confirmation of 1 sent"
#     status1 = getStatus1()

# print "1 confirmed"
# sleep(1)

# bus.write_byte(ard1, 200)
# print "sent 35"
# sleep(4)


# bus.write_byte(ard1, 2)
# try:
#     status1 = getStatus1()
#     print "status1 = %" % status1
# except:
#     print "waiting on 1's status"






