import cv2

img = cv2.imread('Cat/1.jpg')

#imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('original', img)
#cv2.imshow('HSV', imgHSV)
cv2.waitKey(0)