import cv2
import numpy as np

img = cv2.imread('cv_init/Cat/1.jpg')

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow('horizontal', imgHor)
cv2.imshow('vertical', imgVer)

cv2.waitKey(0)