import cv2
cap = cv2.VideoCapture(0)

# define parameters
cap.set(3, 640) #3: width
cap.set(4, 480) #4: height
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#change the brightness
cap.set(10, 100)

# go through wach frame one by one
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('origin',img)
    # add delay to break out the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break