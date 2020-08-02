import cv2
import numpy as np

img = cv2.imread("shapes.jpg")
output = img.copy()
gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1 = 60, param2 = 45, minRadius = 0, maxRadius = 0)
#cv2.imshow("circle", circles)
detected_circles = np.uint16(np.around(circles))

for (x, y, r) in detected_circles[0, :]:
    cv2.circle(output, (x, y), r, (255, 0, 0), 3)
    cv2.circle(output, (x, y), 2, (0, 255, 0), 2)

cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()