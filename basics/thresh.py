import cv2 as cv
from cv2 import threshold
import numpy as np

# Read the image
img = cv.imread('img3.jpg')
cv.imshow("image", img)
# Gray image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# Simple threshold
threshold, thresh = cv.threshold(gray, 150, 250, cv.THRESH_BINARY)
cv.imshow("Simple threshlod", thresh)
# thresh inverse
threshold, thresh_inv = cv.threshold(gray, 150, 250, cv.THRESH_BINARY_INV)
cv.imshow("Threshold_inverse", thresh_inv)
# addapative threshold
addpative_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow("Addpative thresh", addpative_thresh)
cv.waitKey(0)
