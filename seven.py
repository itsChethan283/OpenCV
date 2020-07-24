import cv2
import numpy as np

def click_event(event, x, y, flags, parm):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 1, (0, 0, 255), 1)
        mycolorimg = np.zeros((512, 512, 3), np.uint8)

        mycolorimg[:] = [blue, green, red]
        cv2.imshow("color", mycolorimg)
    
    #if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        #points.append((x, y))
        #if len(points) >=2:
            #cv2.line(img, points[-1], points[-2], (0, 0, 255), 1)
        #cv2.imshow("image", img)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread("lena.jpg", 1)

cv2.imshow("image",img)
points = []

cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()