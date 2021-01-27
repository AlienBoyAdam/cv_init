import cv2
import numpy as np

# read image
img = cv2.imread('Cat/1.jpg')

cv2.imshow('Output', img)
cv2.waitKey(0)




# # read video
# cap = cv2.VideoCapture('video/angel.mp4')

# # go through wach frame one by one
# while True:
#     success, img = cap.read()
#     cv2.imshow('video', img)
    
#     # add delay to break out the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break



# # webcam
# cap = cv2.VideoCapture(0)

# # define parameters
# cap.set(3, 640) #3: width
# cap.set(4, 480) #4: height

# #change the brightness
# cap.set(10, 100)

# # go through wach frame one by one
# while True:
#     success, img = cap.read()
#     cv2.imshow('video', img)
    
#     # add delay to break out the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break




# # convert colors
# img = cv2.imread('Cat/1.jpg')

# #define a kernel
# kernel = np.ones((5,5), np.uint8)

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) # (7,7) is kernel size
# imgCanny = cv2.Canny(img, 150, 200) # find edges
# imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# # cv2.imshow('Gray', imgGray)
# # cv2.imshow('Blur', imgBlur)
# cv2.imshow('Canny', imgCanny)
# cv2.imshow('Dialation', imgDialation)
# cv2.imshow('Eroded', imgEroded)
# cv2.waitKey(0)




# # cropping and resizes
# img = cv2.imread('Cat/1.jpg')
# print(img.shape)

# # resize
# imgResize = cv2.resize(img, (300, 200))
# print(imgResize.shape)

# # crop is same as dealing with an array or matrix
# imgCropped = img[0:200, 200:300]

# cv2.imshow('iamge', img)
# cv2.imshow('resize', imgResize)
# cv2.imshow('cropped', imgCropped)

# cv2.waitKey(0)






# # draw shapes and add texts

# img = np.zeros((512, 512, 3), np.uint8) #3 is color function
# #print(img)
# #img[:] = 255,0,0

# # create line
# cv2.line(img,(0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# # create rectangle
# cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), 2)

# # create circles
# cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

# # put text on images
# cv2.putText(img, 'test text', (300, 200), cv2.FONT_ITALIC, 1, (0, 150, 0), 1)


# cv2.imshow('image', img)

# cv2.waitKey(0)