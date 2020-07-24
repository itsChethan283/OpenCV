import cv2

img = cv2.imread('lena.jpg', 1)
print(img)

cv2.imshow('lena', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('greylena.jpg', cv2.imread('lena.jpg', 0))

cv2.destroyAllWindows()