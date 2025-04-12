import cv2
img = cv2.imread("ment.jpg")
cv2.imshow("ment", img)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
cv2.imshow("Grayscale", gray_image)
cv2.waitKey(0)