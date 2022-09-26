import cv2 as cv
import numpy as np


# read the image
img = cv.imread('img3.jpg')
cv.imshow('image', img)
# convert the grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
# Blur images
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)
# Edge casecade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)
# dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow("Dilated", dilated)
# eroding
erode = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("Eroded", erode)
# resize it
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)
# croppig
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)
cv.waitKey(0)
cv.destroyAllWindows
