import cv2

img = cv2.imread("lena.jpg", 1)

#img = cv2.line(img, (640, 480), (300, 255), (0, 0, 255), 10)
#img = cv2.arrowedLine(img, (0, 0), (255, 255), (0, 0, 255), 10)
#img = cv2.rectangle(img, (255, 255), (355, 355), (0, 0, 255), -1)
#img = cv2.circle(img, (255, 255), 50, (0, 255, 0), 5)  #eclipse(), polylines
img = cv2.putText(img, "simply", (255, 255), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 5, cv2.LINE_AA)

cv2.imshow("lena", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
