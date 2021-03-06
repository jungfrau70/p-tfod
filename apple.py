import cv2
from time import sleep

img_color = cv2.imread('apple.jpg', cv2.IMREAD_COLOR)

# cv2.namedWindow('Show Image')
cv2.imshow('Show Color Image', img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('Show Gray Image', img_gray)
cv2.waitKey(0)

cv2.destroyAllWindows()