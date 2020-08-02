import cv2 
from matplotlib import pyplot as plt

img = cv2.imread("messi5.jpg", 0)
cv2.imshow("image", img)

#plt.imshow(img)
#plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()