import smbus
import time
from time import sleep
import phone_coordinates
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

xVar = 0
yVar = 0


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
    xVar = 0
    yVar = 0

def tap():
    checkStatus()
    bus.write_i2c_block_data(ard1, servoTap, [0,0,0,0])



mode = 0
prompt = "enter x, y, or s: "

while True:
    var = raw_input(prompt)
    try:
        a = int(var)
        print "int"
           
        if mode == 'y':
            yVar = a
            print "moving y to %d" % a
            print "                          %d, %d" %(xVar, yVar)
            prompt = "move y to: "
            y(a)
            
        if mode == 'x':
            xVar = a
            print "moving x to %d" % a
            print "                          %d, %d" %(xVar, yVar)
            prompt = "move x to: "
            x(a)
            
        if mode == 's':
            print "moving servo to %d" % a
            prompt = "move servo to: "
            servo(a)

    except:
        print "string"
        if var == 'x':
            mode = 'x'
            prompt = "mode change! move x to:"
        if var == 'y': 
            mode = 'y'
            prompt = "mode change! movey to:"
        if var == 's':
            mode = 's'
            prompt = "mode change! move servo to:"
        if var == 't':                           # TAP
            print "tappin'"
            tap()
        if (var == 'z'):
            print 'zeroing'
            zero()
        if(var == 'h'):
            print 'home button'
            x(phone_coordinates.homeButton[0])
            y(phone_coordinates.homeButton[1])
            

    

    