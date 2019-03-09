import io
import picamera
import cv2
import numpy

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
#FB like button
roiX = 910
roiXMax = 1120
roiY = 300
roiYMax = 1000

roi = image[roiY:roiYMax,roiX:roiXMax] #  height range, width range (weird)
cv2.rectangle(image,(roiX,roiY),(roiXMax,roiYMax),(0,255,0),1)  # draws box around ROI


#Load a cascade file for detecting faces
heart_cascade = cv2.CascadeClassifier('cascades/reddit_cascade.xml')
# heart_cascade = cv2.CascadeClassifier('heart_cascade_level_16.xml') # for the insta heart cascade
#Convert to grayscale
gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)  # look for hearts within roi

bluramt = 2
blur = cv2.blur(gray,(bluramt,bluramt))
# cv2.imshow('result', blur) # previously image

#Look for faces in the image using the loaded cascade file
minsize = 60
maxsize = 69
hearts = heart_cascade.detectMultiScale(blur,1.05,15,minSize=(minsize,minsize),maxSize=(maxsize,maxsize))
numHearts = len(hearts)
print "Found "+str(numHearts)+" heart(s)"
# if numHearts == 1:
#     print "one heart"
        
#Draw a rectangle around every found heart
for (x,y,w,h) in hearts:
    heartX = roiX + x + w/2  # around the heart plus the distance from the edge to the roi
    heartY = y + h/2
    # cv2.rectangle(image,(x + roiX,y),(x+w + roiX,y+h),(255,0,0),2)
    cv2.rectangle(image,(x + roiX,y + roiY),(x+w + roiX,y+h + roiY),(255,0,0),2)
    # draw a point at the center of the heart

    
    
    # cv2.line(image,(heartX,heartY),(heartX,heartY),(0,0,255),5)
    print "heartX, heartY = (%d, %d)" % (heartX, heartY) 
    print "heartW, heartH = (%d, %d)" % (w,h)

# cv2.rectangle(image,(640,0), (750,camH),(0,255,0),3)

#Save the result image
# cv2.imwrite('result.jpg',image) # previously image
# Show the saved image
cv2.imshow('result', roi) # previously image
cv2.waitKey(0)
cv2.destroyAllWindows()



''' 
heartY 291 = y 5500
heartY 315 = y 5350
heartY 318 = y 5300
hearty 731 = y 3700
heartY 824 = y 3500
'''



