import io
import picamera
import cv2
import numpy
import mapValues
import phone_commands as pc

from time import sleep

def followBack():
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
    roiX = 1050
    roiXMax = 1280
    roiY = 50
    roiYMax = 850
    roi = image[roiY:roiYMax,roiX:roiXMax] #  height range, width range (weird)
    cv2.rectangle(image,(roiX,roiY),(roiXMax,roiYMax),(255,255,255),2) # rect around roi


    #Load a cascade file for detecting follow button
    heart_cascade = cv2.CascadeClassifier('camera/follow_button_cascade_level_9.xml')

    #Convert to grayscale
    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)  # look for hearts within roi

    #Look for faces in the image using the loaded cascade file
    hearts = heart_cascade.detectMultiScale(roi,1.6,10, minSize=(100,100), maxSize=(160,160))  # previously looked at gray instead of cropped roi
    numHearts = len(hearts)
    print "Found "+str(numHearts)+" follow(s)"
    if numHearts > 0:
        
            
        #Draw a rectangle around every found heart
        for (x,y,w,h) in hearts:
            heartX = roiX + x + w/2  # around the heart plus the distance from the edge to the roi
            heartY = roiY + y + h/2
            cv2.rectangle(image,(x + roiX,y + roiY),(x+w + roiX,y+h + roiY),(0,0,0),2)
            # draw a point at the center of the heart
            cv2.line(image,(heartX,heartY),(heartX,heartY),(255,255,255),5)
            

            ''' for whatever reason this haar cascade finds both the blue "follow" and the
            white "following" buttons. The following code determines average color and looks
            for detected buttons that are primarily blue
            '''
            thisHeart = roi[y:y+h,x:x+h]
            # cv2.imwrite('thisHeart.jpg',thisHeart)
            avg_color_per_row = numpy.average(thisHeart, axis=0)
            avg_color = numpy.average(avg_color_per_row, axis=0)
            print(avg_color) #  gives average color of the heart in (B, G, R)
            avg_r_g = (avg_color[1] + avg_color[2] )/2
            print "avg_r_g = %r" % avg_r_g    # the average red and green values
            blue_ratio = avg_color[0] / avg_r_g
            print "blue_ratio = %r" % blue_ratio
            if(blue_ratio > 1.15):
                print "gotta follow this guy"
                cv2.line(image,(heartX,heartY),(heartX,heartY),(0,0,255),5)
            

                print "heartX, heartY = (%d, %d)" % (heartX, heartY) 
                print "heartW, heartH = (%d, %d)" % (w, h)
                toY = mapValues.myMap(heartY)
                print "toY = %d" % toY
                pc.movexy(2650,toY)
                sleep(1)
                pc.lightTap()
                pc.checkStatus()
                # return(toY)
            
            


# # cv2.rectangle(image,(640,0), (750,camH),(0,255,0),3)  # this was used to outline roi

        # #Save the result image
        cv2.imwrite('result.jpg',image) # previously image
        # Show the saved image
        # cv2.imshow('result', roi) # previously image
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
    followBack()
    pc.zero()
