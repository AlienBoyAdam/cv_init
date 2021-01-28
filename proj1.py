import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# define parameters
cap.set(3, 640) #3: width
cap.set(4, 480) #4: height

#change the brightness
cap.set(10, 100)

myColors = [[133, 56, 0, 159, 156, 255],        # pruple
            [57, 76, 0, 100, 255, 255],         # green
            [5, 107, 0, 19, 255, 255]]          # orange

myColorValues = [[153, 0, 153],
                 [0, 204, 0],
                 [0, 255, 128]]  ## BGR

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0;

    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        count += 1;
        # cv2.imshow(str(color[0]), mask)

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print(peri)  # contour param
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            # print(approx)
            # objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

    return x + w//2, y

# go through wach frame one by one
while True:
    success, img = cap.read()
    imgResult = img.copy() 
    findColor(img, myColors, myColorValues)
    cv2.imshow('video', imgResult)
    
    # add delay to break out the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
