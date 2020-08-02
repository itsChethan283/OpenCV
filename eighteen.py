import cv2 

img = cv2.imread("shapes.jpg")
#img.set(3, 720)
#img.set(4, 720)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x - 60, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectratio = float(w) / h
        print(aspectratio)
        if aspectratio >= 0.95 and aspectratio <= 1.05:
            cv2.putText(img, "Square", (x - 60, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
        else:
            cv2.putText(img, "Rectangle", (x - 60, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
    if len(approx) == 5:
        cv2.putText(img, "Pentagon", (x - 60, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
    if len(approx) == 6:
        cv2.putText(img, "Hexagon", (x - 60, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
    if len(approx) > 10:
        cv2.putText(img, "Circle", (x - 60, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()