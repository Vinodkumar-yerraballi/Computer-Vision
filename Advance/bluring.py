import cv2 as cv
import numpy as np


# load the imgae
img = cv.imread('img6.jpg')
cv.imshow('House', img)

# Average blur image
average = cv.blur(img, (3, 3))
cv.imshow('Average blur', average)

# GauusianBllur method natural compare to averages method
gauss = cv.GaussianBlur(img, (9, 9), 0)
cv.imshow("Gaussian blur", gauss)

# meadian blur
median = cv.medianBlur(img, 9)
cv.imshow("Median blur", median)

# bilateral
bilateral = cv.bilateralFilter(img, 5, 25, 35)
cv.imshow("Bilated", bilateral)

cv.waitKey(0)
