import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0);
cap.set(3, 320)
cap.set(4, 320)

cv2.namedWindow("tracker")

cv2.createTrackbar("lh", "tracker", 0, 255, nothing)
cv2.createTrackbar("ls", "tracker", 0, 255, nothing)
cv2.createTrackbar("lv", "tracker", 0, 255, nothing)
cv2.createTrackbar("uh", "tracker", 255, 255, nothing)
cv2.createTrackbar("us", "tracker", 255, 255, nothing)
cv2.createTrackbar("uv", "tracker", 255, 255, nothing)

while True:
    _, img = cap.read()

    #img = cv2.imread("smarties.png", 1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("lh", "tracker")
    ls = cv2.getTrackbarPos("ls", "tracker")
    lv = cv2.getTrackbarPos("lv", "tracker")
    uh = cv2.getTrackbarPos("uh", "tracker")
    us = cv2.getTrackbarPos("us", "tracker")
    uv = cv2.getTrackbarPos("uv", "tracker")

    l_b = np.array([lh, ls, lv])
    u_b = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(img, img, mask = mask)
    cv2.rectangle(res, (0, 0), (20, 20), (0, 0, 0), 4)

    cv2.imshow("image", img)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
    