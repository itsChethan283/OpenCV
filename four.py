import cv2
import datetime
cap = cv2.VideoCapture("Aaluma Doluma.mp4")
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cap.set(3, 720)
#cap.set(4, 720)
#print(cap.get(3))
#print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Widht: '+ str(cap.get(3)) +'Height: '+ str(cap.get(4))
        dt = str(datetime.datetime.now())
        frame = cv2.putText(frame, dt, (0, 40), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == 27:
            break
    else:
        break
        
cap.release()
cv2.destroyAllWindows()

