# works but isn't really useful for phone operator as 


# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (1280, 960)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(1280, 960))
 
# allow the camera to warmup
time.sleep(0.1)

#crops in on image to search for hearts only in the left bit of the phone

#FB like button
roiX = 680
roiXMax = 830
roiY = 300
roiYMax = 1000

# # Twitter like button:
# roiX = 965
# roiXMax = 1100
# roiY = 300
# roiYMax = 1000

# # insta follow back button
# roiX = 955
# roiXMax = 1255
# roiY = 50
# roiYMax = 850

heart_cascade = cv2.CascadeClassifier('cascades/fb_like5.xml') # insta follow back button

# heart_cascade = cv2.CascadeClassifier('cascades/fb_like3.xml') # fb like cascade 

# heart_cascade = cv2.CascadeClassifier('cascades/twit_heart3.xml') # twitter heart one


# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    roi = image[roiY:roiYMax,roiX:roiXMax] #  height range, width range (weird)

    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    
    bluramt = 2

    blur = cv2.blur(gray,(bluramt,bluramt))
    minsize = 60
    maxsize = 69
    hearts = heart_cascade.detectMultiScale(blur,1.05,20,minSize=(minsize,minsize),maxSize=(maxsize,maxsize))
    numHearts = len(hearts)

    for (x,y,w,h) in hearts:
        heartX = x + w/2  # around the heart plus the distance from the edge to the roi
        heartY = y + h/2
        # cv2.rectangle(image,(x + roiX,y),(x+w + roiX,y+h),(255,0,0),2)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2)
        # draw a point at the center of the heart
        print w, " ", h



    # show the frame
    cv2.imshow("Frame", roi)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
      break