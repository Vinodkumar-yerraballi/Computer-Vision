
from turtle import width
import cv2 as cv
import numpy as np
img = cv.imread('img2.jpg')
cv.imshow("image", img)
# rescale the frame


def rescaleFrame(fram, scale=0.75):
    width = int(fram.shape[1]*scale)
    height = int(fram.shape[0]*scale)
    diemension = (width, height)
    return cv.resize(fram, diemension, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(0)
# create while loop
while True:
    isTrue, fram = capture.read()
    frame_resized = rescaleFrame(fram, scale=0.2)
    cv.imshow('video', fram)
    cv.imshow("video_resized", frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.realse()
# cv.waitKey(0)
cv.destroyAllWindows
