import cv2

img = cv2.imread("sudoku.png", 0)
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 93, 16)

cv2.imshow("th1", th1)

cv2.waitKey(0)
cv2.destroyAllWindows()