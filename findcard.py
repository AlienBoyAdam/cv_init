import cv2
import numpy as np

img = cv2.imread('Card/card.jpg')

width, height = 250, 350

# define four conor points
pts1 = np.float32([[175, 73], [338, 106], [124, 299], [289, 334]])
# define the original point
pts2 = np.float32([[0,0],[width, 0],[0, height],[width, height]])
# transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('image', img)
cv2.imshow('output', imgOutput)

cv2.waitKey(0)