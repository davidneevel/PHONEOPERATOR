# this was the original code, before i moved everything into the 
# PHONEOP / phone_commands / phone coordinates scripts

import smbus   # was smbus in the original sketch, replaced with smbus2 because you can't pip smbus
import phone_commands as pc

# first byte values! for the first byte sent to arduino
moveY = 1
moveX = 2
servoUp = 3
servoDown = 4
servoTap = 5
servoTo = 6
zero = 7
moveXY = 8
servoSlowTap = 9
servoLightTap = 10
onOffCmd = 11

import time
from time import sleep
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
ard1 = 0x04


def checkStatus(): # checks and waits until not busy
    gettingStatus = 1;
    while gettingStatus == 1:
        try:
            status = bus.read_byte(ard1)
            if status == 100:    # 100 means ready
                print "ard1 ready"
                gettingStatus = 0
            else:
                print "ard1 busy"
                sleep(.1)
        except:
            print "ard1 is offline. trying again"
            sleep(.1)



def xy(x ,y):
    checkStatus()
    b = int(round(x/100))
    c = x - (b * 100)
    d = int(round(y/100))
    e = y - (d * 100)
    bus.write_i2c_block_data(ard1,moveXY,[b,c,d,e])
    # sleep(.1)
def y(value):
    checkStatus()
    b = int(round(value/100))
    # print "b = %d" % b
    c = value - (b * 100)
    # print "c = %d" %c
    bus.write_i2c_block_data(ard1,moveY,[b,c,0,0])
    sleep(.01)
    
def x(value):
    checkStatus()   # is arduino busy?
    b = int(round(value/100))
    c = value - (b * 100)
    bus.write_i2c_block_data(ard1, moveX,[b,c,0,0])
    sleep(.01)

def servo(value):
    checkStatus()
    bus.write_i2c_block_data(ard1, servoTo,[0,value,0,0])
    print servoTo
    print 0
    print value
    sleep(.01)

def zero():
    checkStatus()
    bus.write_i2c_block_data(ard1, 7,[0,0,0,0])

def tap():
    print "tapping"
    checkStatus()
    bus.write_i2c_block_data(ard1, servoTap, [0,0,0,0])
    checkStatus()

def slowTap():
    print "slow tap"
    checkStatus()
    bus.write_i2c_block_data(ard1, servoSlowTap, [0,0,0,0])
    checkStatus()

def lightTap():
    print "light tap"
    checkStatus()
    bus.write_i2c_block_data(ard1, servoLightTap, [0,0,0,0])
    checkStatus()

def onOff():
    print "onOff"
    checkStatus()
    bus.write_i2c_block_data(ard1, onOffCmd, [0,0,0,0])
    checkStatus()



# STARTING

# #check on arduino 1
status1 = 0

checkStatus()



# arduinos are online! available to be moved 
checkStatus()


zero()

xy(2100, 2400)  # home button

tap()

sleep(.75)

tap()
sleep(.25)

y(3700) # 0
tap()
y(4800)  #5
tap()
y(5300)  # 2
tap()
xy(1500,4800)
tap()          #4

xy(2350,5950)  # instagram app
tap()

xy(2100,2800)  # make post button
tap()
sleep(1)
xy(1150,4400)  # selfie cam button
tap()
sleep(1)


xy(2100, 3600) # take picture
tap()
sleep(1.5)

xy(3050, 6650)  # next button
sleep(.25)
tap()

xy(2100, 6300)  # enter text
tap()
sleep(1)

xy(3100,3500) # L
lightTap()
sleep(.25)

xy(2950,3900) # O
lightTap()
sleep(.25)

xy(3100,3500) # L
lightTap()
sleep(.25)

xy(3050,6650) # OK
sleep(.25)
slowTap()

sleep(1)

slowTap()  #  POST

xy(2100,2400) # home button
sleep(5)
xy(2100,4300)
tap()
sleep(.15)
tap()
xy(2100,2400)  #home button
sleep(1)
tap()

sleep(2)

onOff()


zero()


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




def signal_handler(signal, frame):
    zero()
    print 'You pressed Ctrl+C!'
    sys.exit(0)

