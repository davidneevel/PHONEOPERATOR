import smbus   

import time
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)
var = 0
# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
    
    # bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    bus.write_i2c_block_data(address, 1, [255, 255] )
    return -1

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number

while True:
    try:
        var = int(raw_input("Enter 1 - 9: "))
    except ValueError:
        print "Could you at least give me an actual number?"
        continue 

    writeNumber(var)
    print "RPI: Hi Arduino, I sent you ", var
    # sleep one second
    #time.sleep(1)

    number = readNumber()
    print "Arduino: Hey RPI, I received a digit ", 
    print number
    # print chr(number)  # this is how you decode into an ascii symbol
  
    print