import cv2
import threading
import time

class VideoStream:
    def __init__(self, src):
        self.cap = cv2.VideoCapture(src)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.ret, self.frame = self.cap.read()
        self.running = True
        threading.Thread(target=self._update, daemon=True).start()

    def _update(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.ret, self.frame = ret, frame
            else:
                time.sleep(0.005)

    def read(self):
        return self.ret, self.frame

    def stop(self):
        self.running = False
        self.cap.release()

#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap = VideoStream(
    "http://192.168.1.34:4747/video"
)
time.sleep(0.5)

LlaveClassif = cv2.CascadeClassifier(
    'cascade.xml'
)

while True:

    ret, frame = cap.read()
    if not ret or frame is None:
        continue

    frame = cv2.resize(frame, (640, 480))

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    alto, ancho = gray.shape
    cv2.rectangle(gray, (0, int(alto * 0.78)), (int(ancho * 0.55), alto), (128, 128, 128), -1)

    llave = LlaveClassif.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=35,
        minSize=(120, 56)
    )

    for (x,y,w,h) in llave:

        margen_x = int(w * 0.25)
        margen_y = int(h * 0.20)

        x1 = max(x - margen_x, 0)
        y1 = max(y - margen_y, 0)

        x2 = x + w + margen_x
        y2 = y + h + margen_y

        cv2.rectangle(
            frame,
            (x1,y1),
            (x2,y2),
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            'Llave_Inglesa',
            (x1,y1-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2,
            cv2.LINE_AA
        )

    cv2.imshow(
        'frame',
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.stop()
cv2.destroyAllWindows()
