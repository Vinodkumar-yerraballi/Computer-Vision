import cv2 as cv
from cv2 import rectangle
from cv2 import circle
from cv2 import bitwise_and
from cv2 import bitwise_or
import numpy as np


# load the imgae
img = cv.imread('img6.jpg')
cv.imshow('House', img)
# blank
blank = np.zeros((400, 400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow('Rectangle', rectangle)
cv.imshow("circle", circle)

# bitwise-and-intersecting region
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise_and", bitwise_and)

# bitwise_or
# non interseting  and interseting
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise_or", bitwise_or)


# bitwise_xor
# non interseting
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise_xor", bitwise_xor)

# bitwise_xor
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwise_not", bitwise_not)

# bitwise_xor
bitwise_not = cv.bitwise_not(circle)
cv.imshow("bitwise_not", bitwise_not)

cv.waitKey(0)
