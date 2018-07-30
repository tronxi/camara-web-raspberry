"""from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)
 
time.sleep(0.1)
 
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
 
cv2.imshow("Image", image)
cv2.waitKey(0)"""

import cv2
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        
        cv2.imshow("Camara", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows() 