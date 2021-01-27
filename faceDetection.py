# using Viola & Jones
# Collecting positive and negative faces to train and generate an XML file

import cv2
path = 'faces/faces.jpg'
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.resize(cv2.imread(path), (1200, 600))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('origin',img)
cv2.waitKey(0)