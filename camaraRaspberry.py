import numpy as np
import cv2

video_file = 'examples/videos/roller-coaster.mp4'
cap = cv2.VideoCapture(0)
fondo = None
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