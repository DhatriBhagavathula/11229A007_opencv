import cv2
img = cv2.imread("ment.jpg")
cv2.imshow("ment.jpg", img)
cv2.imwrite("ment.png", img)
cv2.imwrite("ment.tiff", img)
cv2.imshow("ment.png", img)
cv2.imshow("ment.tiff", img)
cv2.waitKey(0)