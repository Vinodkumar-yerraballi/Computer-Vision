import cv2 as cv
from cv2 import circle
import numpy as np


# load the imgae
img = cv.imread('img7.jpg')
cv.imshow('House', img)
# blank
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("blank image", blank)
# mask the mask
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("mask", circle)

#
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)
# masked
masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow('masked', masked)

cv.waitKey(0)
