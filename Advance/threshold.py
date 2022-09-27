import cv2 as cv
from cv2 import threshold
import numpy as np

img = cv.imread('img6.jpg')
cv.imshow('House', img)

# Convert the gray scale img

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresh_inv", thresh_inv)

# addaptive threshlod
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive_thresh", adaptive_thresh)

cv.waitKey(0)
