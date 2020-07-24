import cv2
import time

cap = cv2.VideoCapture("Aaluma Doluma.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')          #or ('x','v','i','d')
out = cv2.VideoWriter("two.avi", fourcc, 20.0, (640, 480))          #("name", format, framespersec, size)
m = cap.isOpened()
print(m)
time.sleep(3)

while m:
    ret, frame = cap.read()
    if ret == True:
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('camera', gray)

        out.write(frame)                            #name.write(frame)

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    #name.get(cv2.nameof the property)
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        k = cv2.waitKey(1)

        if k == 27:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
    