import smbus
import phone_coordinates as xy

bus = smbus.SMBus(1)

ard1 = 0x04
# first byte values! for the first byte sent to arduino
moveY = 1
moveX = 2
servoUp = 3
servoDown = 4
servoTap = 5
servoTo = 6
zeroCmd = 7
moveXY = 8
servoSlowTap = 9
servoLightTap = 10
onOffCmd = 11


from time import sleep
print "commands imported"

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


def movexy(x,y):           # for x, y coordinates
    checkStatus()
    b = int(round(x/100))
    c = x - (b * 100)
    d = int(round(y/100))
    e = y - (d * 100)
    bus.write_i2c_block_data(ard1,moveXY,[b,c,d,e])

def move(value):          # for predefined locations specified in phone_coordinates
    x = value[0]
    y = value[1]
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
    bus.write_i2c_block_data(ard1, zeroCmd,[0,0,0,0])

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

def onOff():     # hits side power button once
    print "onOff"
    checkStatus()
    bus.write_i2c_block_data(ard1, onOffCmd, [0,0,0,0])
    checkStatus()

def scrollUp():
    checkStatus()
    move(xy.np0)
    sleep(.25)
    servo(xy.servoDownSuperLight)
    sleep(.1)
    move(xy.np2)
    servo(xy.servoUp)
    # move(xy.np0)
    checkStatus()

def getOutTheWay():
    checkStatus()
    move(xy.homeButton)
    checkStatus()

def homeButton():
    move(xy.homeButton)
    tap()


def unlock():
    zero()

    move(xy.homeButton)  # home button

    tap()

    sleep(.75)
    tap()
    sleep(.35)

    move(xy.np0)
    tap()
    move(xy.np5)
    tap()
    move(xy.np2)
    tap()
    move(xy.np4)
    tap()
    sleep(1)  # phone opens
    
def press(value):
    move(value)
    lightTap()

def text_mike():
    move(xy.app(0,6))
    lightTap()
    movexy(2200,5850)   # text field
    tap()
    press(xy.m)
    press(xy.i)
    press(xy.k)
    press(xy.e)
    movexy(2200,5950)
    lightTap()
    movexy(2200, 3050)
    sleep(1)
    tap()
    press(xy.h)
    press(xy.e)
    press(xy.y)
    press(xy.space)
    press(xy.m)
    press(xy.i)
    press(xy.k)
    press(xy.e)
    press(xy.space)
    press(xy.w)
    press(xy.h)
    press(xy.a)
    press(xy.t)
    press(xy.numbers)
    press(xy.m)       # apostrophe is near the m key
    press(xy.s)
    press(xy.space)
    press(xy.u)
    press(xy.p)
    press(xy.numbers)
    press(xy.v)   # question mark
    movexy(3150,4400) # send button
    sleep(1)
    tap()
    move(xy.homeButton)
    sleep(5)
    tap()
    zero()


def respond_to_text():
    move(2100,5400)
    tap()
    move(2100, 3050)
    sleep(1)
    press(xy.n)
    press(xy.i)
    press(xy.c)
    press(xy.e)

def type(a):
    length = len(a)
    for i in range(0,length):
        letter = a[i]
        if letter == ' ':
            move(xy.space)
        elif letter == '1':
            move(xy.one)
        elif letter == '2':
            move(xy.two)
        elif letter == '3':
            move(xy.three)
        elif letter == '4':
            move(xy.four)
        elif letter == '5':
            move(xy.five)
        elif letter == '6':
            move(xy.six)   
        elif letter == '7':
            move(xy.seven)
        elif letter == '8':
            move(xy.eight)
        elif letter == '9':
            move(xy.nine)
        elif letter == '0':
            move(xy.zero)
        
        else:
            varname = 'xy.' + letter
            target = eval(varname)
            move(target)
        lightTap()

    
def twitter():
    move(xy.app(3,2))  # twitter app
    tap()
    move((3100,6500))   # new tweet button
    tap()
    sleep(1)

    move(xy.c)
    lightTap()
    move(xy.h)
    lightTap()
    move(xy.e)
    lightTap()
    move(xy.c)
    lightTap()
    move(xy.k)
    lightTap()
    move(xy.space)
    lightTap()
    move(xy.o)
    lightTap()
    move(xy.u)
    lightTap()
    move(xy.t)
    lightTap()
    move(xy.space)
    lightTap()
    move(xy.m)
    lightTap()
    move(xy.y)
    lightTap()
    move(xy.space)
    lightTap()
    move(xy.n)
    lightTap()
    move(xy.e)
    lightTap()
    move(xy.w)
    lightTap()
    move(xy.space)
    lightTap()
    move(xy.v)
    lightTap()
    move(xy.i)
    lightTap()
    move(xy.d)
    lightTap()
    move(xy.e)
    lightTap()
    move(xy.o)
    lightTap()
    move(xy.space)
    lightTap()
    move(xy.o)
    lightTap()
    move(xy.n)
    lightTap()
    move(xy.space)
    lightTap()
    move(xy.i)
    lightTap()
    move(xy.n)
    lightTap()
    move(xy.s)
    lightTap()
    move(xy.t)
    lightTap()
    move(xy.a)
    lightTap()
    move(xy.g)
    lightTap()
    move(xy.r)
    lightTap()
    move(xy.a)
    lightTap()
    move(xy.m)
    lightTap()
    sleep(5)

    move((3000,6500))   # post button
    tap()


    move(xy.homeButton)  # home button

    tap()

    zero()




def insta_selfie():

    move(xy.app(2,1))  # instagram app
    tap()

    movexy(1950,2700)  # make post button
    tap()
    sleep(1)
    movexy(950,4150)  # selfie cam button
    tap()
    sleep(1)


    movexy(1950, 3450) # take picture
    tap()
    sleep(1.5)

    movexy(2800, 6450)  # next button
    sleep(.25)
    tap()

    movexy(2100, 6100)  # enter text
    tap()
    sleep(1)

    move(xy.l) # L
    lightTap()
    sleep(.25)

    move(xy.o) # O
    lightTap()
    sleep(.25)

    move(xy.l) # L
    lightTap()
    sleep(.25)

    movexy(2800, 6450) # OK
    sleep(.25)
    slowTap()

    sleep(1)

    slowTap()  #  POST

    move(xy.homeButton) # home button
    sleep(5)

    tap()

    sleep(2)

    onOff()


    zero()


def off():
    zero()
    onOff()

def open_insta_followers():
    
    move(xy.app(2,1))
    tap()
    movexy(2850, 2700)
    tap()
    movexy(2200, 6100)
    tap()
    move(xy.homeButton)
 
