from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera
import time
import cv2
import base64
import signal
import sys

from urllib.parse import urlencode 
from urllib.request import Request, urlopen

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
def signal_handler(sig, frame):  
        enviarImagen(cv2.imread("error.jpg"))
        time.sleep(1)
        sys.exit(0)
        
def enviarImagen(imagen):
    codificado_correctamente, buffer = cv2.imencode('.png', imagen)

    if codificado_correctamente:
        imagen_en_base64 = base64.b64encode(buffer).decode('utf-8')
        url = 'http://192.168.0.5/camara-web-web/php/subirImagen.php'
        datos_enviar = {'imagen': imagen_en_base64}
        peticion = Request(url, urlencode(datos_enviar).encode())
        urlopen(peticion)
        time.sleep(0.5)
        rawCapture.truncate(0)
    else:
        print("error al codificar")
def buscarCaras(imagen):
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        imagen = cv2.rectangle(imagen, (x,y), (x+w, y+h), (255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = imagen[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return imagen

signal.signal(signal.SIGINT, signal_handler)

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
 
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    imagen = cv2.flip(frame.array, 0)
    enviarImagen(buscarCaras(imagen))


