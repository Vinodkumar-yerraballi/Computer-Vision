import cv2 as cv
import numpy as np


# Load the image
img = cv.imread('img6.jpg')
cv.imshow("house", img)
# blank the images
blank = np.zeros(img.shape[:2], dtype='uint8')
# bgr
b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merged rgb
merged = cv.merge([r, g, b])
cv.imshow('Merged', merged)

# merage the all channel
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


cv.waitKey(0)
