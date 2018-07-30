import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fondo = None
if(cap.isOpened()):
    print("funciona")
else:
    print("error")
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