
def myMap(a):  # trying to recreate arduino's map function here
    b = 0.0
    b = a - 291.0   # take out the offset. 291 is (a little less than) the min value it will deliver.
    print "b minus offset: %d" % b
    inRange = 0.0
    inRange = 824 - 291
    inRange = inRange * 1.0
    print "inRange = %d" % inRange
    intRatio = 0.0
    inRatio = b / inRange # the distance through the in range a is
    print "inRatio = %d" % inRatio
    outRange = 5500 - 3500
    print "outRange = %d" % outRange
    outRatio = inRatio * outRange
    print "outRatio = %d" % outRatio
    out = 5500 - outRatio
    print "out = %d" % out

myMap(315)

a = 440
b = 533.0
c = a/b
print c


''' 
heartY 291 = y 5500
heartY 315 = y 5350
heartY 318 = y 5300
hearty 731 = y 3700
heartY 824 = y 3500
'''

