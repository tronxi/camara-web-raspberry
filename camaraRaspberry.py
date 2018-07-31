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

def signal_handler(sig, frame):  
        enviarImagen(cv2.imread("error.jpg"))
        sys.exit(0)
        
def enviarImagen(imagen):
    codificado_correctamente, buffer = cv2.imencode('.png', imagen)

    if codificado_correctamente:
        imagen_en_base64 = base64.b64encode(buffer).decode('utf-8')
        url = 'http://192.168.0.5/camara-web-web/php/subirImagen.php'
        datos_enviar = {'imagen': imagen_en_base64}
        peticion = Request(url, urlencode(datos_enviar).encode())
        urlopen(peticion)
    else:
        print("error al codificar")

    #

signal.signal(signal.SIGINT, signal_handler)

"""camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    enviarImagen(cv2.flip(frame.array, 0))
    rawCapture.truncate(0)"""


with picamera.PiCamera() as picam:
    picam.resolution = (2592, 1944)
    while True:
        time.sleep(0.5)
        picam.capture('imagen.png', resize=(640, 480))
        imagen = cv2.imread('imagen.png')
        enviarImagen(imagen)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
"""cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow("Camara", frame)
        time.sleep(0.2)
        enviarImagen(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break"""



