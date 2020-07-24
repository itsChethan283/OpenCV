import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow("image")

cv.createTrackbar("b", "image", 0, 255, nothing)
cv.createTrackbar("g", "image", 0, 255, nothing)
cv.createTrackbar("r", "image", 0, 255, nothing)

switch = "0 or 1"
cv.createTrackbar(switch, "image", 0, 1, nothing)

while True:
    cv.imshow("image", img)
    k = cv.waitKey(1)
    if k == 27:
        break

    b = cv.getTrackbarPos("b", "image")
    g = cv.getTrackbarPos("g", "image")
    r = cv.getTrackbarPos("r", "image")

    s = cv.getTrackbarPos(switch, "image")
    if s == 1:
        img[:] = [b, g, r]
    else:
        img[:] = [0]

cv.destroyAllWindows()