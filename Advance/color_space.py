import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# load the image
img = cv.imread('img5.jpg')
cv.imshow("House", img)
# Let's visualize the image using the matplotlib
# plt.imshow(img)
# plt.show()
# Cover the image BGR to Gray color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# Covert the BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
# Covert the BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
# Covert the BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
# we ca't covert the gray to HSV direatly then we firstly covert the HSV to BGR
# Covert the hsv to bgr
hsv_bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('HSV', hsv_bgr)

cv.waitKey(0)
