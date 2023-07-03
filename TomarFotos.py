import cv2
import numpy as np
import imutils
import os

carpeta = input("Ingrese p si es positivo o n si es negativo: ")
if not os.path.exists(carpeta):
	print('Carpeta creada: ', carpeta)
	os.makedirs(carpeta)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

x1, y1 = 190, 80
x2, y2 = 450, 398

archivos = os.listdir(carpeta)
count =  len(archivos)

while True:

	ret, frame = cap.read()
	if not ret:
		break

	imAux = frame.copy()
	cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

	objeto = imAux[y1:y2, x1:x2]
	objeto = imutils.resize(objeto, width=38)

	k = cv2.waitKey(1)
	if k == ord('s'):
		cv2.imwrite(carpeta + '/{}.jpg'.format(count), objeto)
		print('Imagen almacenada: ', '{}.jpg'.format(count))
		count = count + 1
	if k & 0xFF == ord('q'):
		break

	cv2.imshow('frame', frame)

cap.release()
cv2.destroyAllWindows()
