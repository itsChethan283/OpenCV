import cv2

img = cv2.imread("messi5.jpg", 1)
img1 = cv2.imread("opencv-logo.png", 1)

print(img.shape)  #returns a tuple with number of rows, columns and channels
print(img.size)   #returns number of pixles
print(img.dtype)  #returns datatype

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))             

ball = img[280: 340, 330: 390]
img[273: 333, 100: 160] = ball 

img = cv2.resize(img, (512, 512))
img1 = cv2.resize(img1, (512, 512))

#both = cv2.add(img, img1)
both = cv2.addWeighted(img, 0.9, img1, 0.1, 0)

cv2.imshow("image", both)
cv2.waitKey(0)
cv2.destroyAllWindows()