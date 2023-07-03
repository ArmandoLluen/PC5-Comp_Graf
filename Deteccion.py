import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
clasificador = cv2.CascadeClassifier('cascade.xml')

while True:

    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    toy = clasificador.detectMultiScale(gray,
                                        scaleFactor=8,
                                        minNeighbors=100,
                                        minSize=(70, 70))

    for (x, y, w, h) in toy:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Juguete', (x, y), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Heer Cascade', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()