import io
import picamera
import cv2
import numpy
import mapValues
import phone_commands as pc

import random

from time import sleep

def lookForHearts():
    #Create a memory stream so photos doesn't need to be saved in a file
    stream = io.BytesIO()
    
    camW = 1280
    camH = 960
    
    #Get the picture (low resolution, so it should be quite fast)
    #Here you can also specify other parameters (e.g.:rotate the image)
    with picamera.PiCamera() as camera:
        camera.resolution = (camW,camH)   #   4:3 1280:960 also works
        camera.capture(stream, format='jpeg')

    #Convert the picture into a numpy array
    buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

    #Now creates an OpenCV image
    image = cv2.imdecode(buff, 1)

    #crops in on image to search for hearts only in the left bit of the phone
    roiX = 640
    roiY = 300
    roiYMax = 800
    roi = image[roiY:roiYMax,640:750] #  height range, width range (weird)

    #Load a cascade file for detecting faces
    heart_cascade = cv2.CascadeClassifier('camera/heart_cascade_level_16.xml')

    #Convert to grayscale
    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)  # look for hearts within roi

    #Look for faces in the image using the loaded cascade file
    hearts = heart_cascade.detectMultiScale(roi)  # previously looked at gray instead of cropped roi
    numHearts = len(hearts)
    print "Found "+str(numHearts)+" heart(s)"
    if numHearts == 1:
        print "one heart"
            
        #Draw a rectangle around every found heart
        for (x,y,w,h) in hearts:
            heartX = roiX + x + w/2  # around the heart plus the distance from the edge to the roi
            heartY = roiY + y + h/2
            cv2.rectangle(image,(x + roiX,y + roiY),(x+w + roiX,y+h + roiY),(255,0,0),2)
            # draw a point at the center of the heart
            
            cv2.line(image,(heartX,heartY),(heartX,heartY),(0,0,255),5)
            cv2.imwrite('result.jpg',image)   # save image
            print "heartX, heartY = (%d, %d)" % (heartX, heartY) 
            toY = mapValues.myMap(heartY)
            print "toY = %d" % toY
            pc.movexy(900,toY)
            pc.lightTap()
            pc.checkStatus()
            b = random.randint(1,100)

            #tapped the heart, now decide whether to comment or not
            print "random number = %d" % b
            if b <= 20:
                pc.x(1100)  # move over to the comment button
                pc.tap()
                pc.type("nice")
                pc.movexy(2800, 4300)  #post comment
                pc.tap()
                sleep(2)
                pc.movexy(900, 6300)  # back to stream
                pc.tap()
            if b > 20 and b <= 40:
                pc.x(1100)  # move over to the comment button
                pc.tap()
                pc.type('great pic')
                pc.movexy(2800, 4300)  #post comment
                pc.tap()
                sleep(2)
                pc.movexy(900, 6300)  #back to stream
                pc.tap()
            return(toY)
            
    
    else:
        print "no hearts found"
            
            


# # cv2.rectangle(image,(640,0), (750,camH),(0,255,0),3)  # this was used to outline roi

# #Save the result image
# cv2.imwrite('result.jpg',image) # previously image
# # Show the saved image
# cv2.imshow('result', image) # previously image
# cv2.waitKey(0)
# cv2.destroyAllWindows()





''' 
heartY 291 = y 5500
heartY 315 = y 5350
heartY 318 = y 5300
hearty 731 = y 3700
heartY 824 = y 3500
'''

if __name__ == "__main__":
    pc.zero()               #put the zeros in here so it doesn't zero while scrolling
    lookForHearts()
    pc.zero()
