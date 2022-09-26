from this import d
import cv2 as cv
import numpy as np


# load the image
img = cv.imread('img1.jpg')
#cv.imshow('Images', img)

#Drawing and write
blank = np.zeros((500, 500, 3), dtype='uint8')
# bank the webpage
blank[:] = 0, 255, 0
# create the box with green color
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Green', blank)
# let's draw the rectangle for the shape
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=-1)
cv.imshow('recatangle', blank)
# draw the circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
          40, (0, 0, 255), thickness=-1)
cv.imshow('circle', blank)
# Draw the line
cv.line(blank, (0, 0),
        (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=14)
cv.imshow('line', blank)
# write the text to the
cv.putText(blank, "Hello i'm vinod!!!", (225, 225),
           cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 250, 2), 2)
cv.imshow('Text', blank)
cv.waitKey(0)
cv.destroyAllWindows
