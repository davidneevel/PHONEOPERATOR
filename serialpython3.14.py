import serial
from time import sleep
a = 0
ser = serial.Serial('/dev/ttyUSB0', 9600)

ser.write('ass')

while 1:
    a += 1
    ser.write(a)
    var = ser.readline()
    print var
    ser.readline()
    sleep(.1)
