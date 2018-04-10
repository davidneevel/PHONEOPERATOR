
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (1024, 768)
rawCapture = PiRGBArray(camera)
 
# allow the camera to warmup
time.sleep(0.1)
 
# grab an image from the camera
camera.capture(rawCapture, format="bgr")
camera.capture('pythoncapture.jpg')
image = rawCapture.array
 
# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)