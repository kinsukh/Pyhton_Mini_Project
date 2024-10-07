import cv2

def take_picture():
    imgcap = cv2.VideoCapture(0)

    result = True
    while result:
        ret, frame = imgcap.read()
        cv2.imwrite('test.jpg',frame)
        result = False
        print(" done imgae captured...")
        
    imgcap.release()

def video_cam():   
    imgcap = cv2.VideoCapture(0)

    while(True):
        ret, frame = imgcap.read()

        cv2.imshow('video', frame)
        print(" press 'q' to stop the video")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    imgcap.release()
    cv2.destroyAllWindows()