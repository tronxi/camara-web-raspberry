import cv2

cap = cv2.VideoCapture(0)

leido, frame = cap.read()

if leido == True:
    cv2.imwrite("prueba.png", frame)
else:
    print("error al acceder a la camara")
cap.release()