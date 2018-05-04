#server receives messages!

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


downPin = 38
upPin = 40

prevMessage = "neutral"

GPIO.setup(upPin,GPIO.OUT)
GPIO.setup(downPin,GPIO.OUT)

import OSC
listenIP="192.168.1.105"   # NB!!! THIS IS THE SERVER'S ADDRESS! NOT THE CLIENT'S! FUCK!
port = 49159

def handler(addr, tags, data, client_address):
#    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
#    txt += str(data)
#    print(txt)
    print addr

def ballshandler(addr, tags, data, client_address):
    print "we got a balls message"
    print data
    if data == ['up']:
        global prevMessage
        #if prevMessage == "neutral":
#            print "backing up"
#            GPIO.output(downPin, GPIO.HIGH)
#            sleep(.1)
#            GPIO.output(downPin, GPIO.LOW)
#            print "up"
#            sleep(.1)
        GPIO.output(upPin, GPIO.HIGH)
        prevMessage = 'up'

    if data == ["text_mike"]:
        
        print "going to text mike"
        import phone_commands as pc
        sleep(1)
        pc.text_mike()


   


if __name__ == "__main__":
    s = OSC.OSCServer((listenIP, port))  # listen on listenIP, port xxxx
    print 'listening to %s, port %d' % (listenIP, port)
    
    s.addMsgHandler('/startup', handler)     # call handler() for OSC messages received with the /startup address
    s.addMsgHandler('/balls', ballshandler)
    
    s.serve_forever()
    