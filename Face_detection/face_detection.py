import cv2 as cv
import numpy as np

# load the image
img = cv.imread('download (1).jpeg')
cv.imshow('Man', img)
# covert the image to gryscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
haar_cassed = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
face_ret = haar_cassed.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'Number of face found ={len(face_ret)}')
for (x, y, w, h) in face_ret:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow("detected image", img)


cv.waitKey(0)
