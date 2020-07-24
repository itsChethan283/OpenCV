import numpy as np
import cv2 as c

def nothing(x):
    print(x)

#c.imshow("image", img)
c.namedWindow("image")
c.createTrackbar("cp", "image", 0, 255, nothing)

switch = "color/gray"
c.createTrackbar(switch, "image", 0, 1, nothing)

while True:
    img = c.imread("lena.jpg", 1)
    pos = c.getTrackbarPos("cp", "image")
    c.putText(img, str(pos), (200,200), c.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)

    p = c.getTrackbarPos(switch, "image")

    if p== 1:
        img = c.cvtColor(img, c.COLOR_BGR2GRAY)
    else:
        pass

    c.imshow("image", img)
    
    k = c.waitKey(1)
    if k == 27:
        break

c.destroyAllWindows()