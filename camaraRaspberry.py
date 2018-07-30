from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import base64

from urllib.parse import urlencode 
from urllib.request import Request, urlopen

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    image = frame.array
    #
    codificado_correctamente, buffer = cv2.imencode('.png', image)
	if codificado_correctamente:
        imagen_en_base64 = base64.b64encode(buffer).decode('utf-8')

		url = 'http://192.168.0.5/camara-web-web/php/subirImagen.php'
		datos_enviar = {'imagens': imagen_en_base64}

		print("Enviando foto...")

		peticion = Request(url, urlencode(datos_enviar).encode())
		respuesta = urlopen(peticion).read().decode()
		
		print("Guardada con éxito")
    #
    cv2.imshow("Image", image)

    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break