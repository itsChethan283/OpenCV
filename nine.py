import cv2
import numpy as np

img1 = np.zeros((900, 900, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (700, 100), (255, 255, 255), -1)
img2 = cv2.imread("image_1.jpg", 1)

#bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)

cv2.imshow("image 1", img1)
cv2.imshow("image 2", img2)
#cv2.imshow("bitand", bitAnd)
cv2.imshow("bitor", bitOr)

cv2.waitKey(0)
cv2.destroyAllWindows()
