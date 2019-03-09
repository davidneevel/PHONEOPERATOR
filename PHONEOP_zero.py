import smbus   # was smbus in the original sketch, replaced with smbus2 because you can't pip smbus

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





def zero():
    checkStatus()
    bus.write_i2c_block_data(ard1, 7,[0,0])



# STARTING

# #check on arduino 1
status1 = 0


zero()




