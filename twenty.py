import cv2
import numpy as np

img = cv2.imread("messi5.jpg", 1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

temp = cv2.imread("messi5_face.jpg", 0 )
w, h = temp.shape[::-1]

res = cv2.matchTemplate(gray_img, temp, cv2.TM_CCOEFF_NORMED)
#print(res)

threshold = 0.95;
loc = np.where(res >= threshold)
print(loc[0])

for pt in zip(*loc[::-1]):
    print("chethan")

    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (255, 255, 2), 2)

cv2.imshow("image", img)
cv2.waitKey(0)

cv2.destroyAllWindows()