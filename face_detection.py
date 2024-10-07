import cv2

face_casscade = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")

def detect():
    cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face = face_casscade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) 

        cv2.imshow("Face Detection", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    cap.release()

detect()