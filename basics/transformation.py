from turtle import width
import cv2 as cv
import numpy as np

img = cv.imread('img3.jpg')
#cv.imshow("image", img)

# translatio


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])  # type: ignore
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)


translate = translate(img, 100, 00)
#cv.imshow("translated", translate)
cv.waitKey(0)
cv.destroyAllWindows
# -x--->left
# -y--->up
# x--->right
# y-->down

# Rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimension = (width, height)
        return cv.warpAffine(img, rotMat, dimension)


# define the rotation
rotated = rotate(img, 45)
cv.imshow("rotated", rotated)
# rotate the image negative direaction
rotated_rotated = rotate(img, -45)
cv.imshow("rotated_rotated", rotated_rotated)
# Resized
resized = cv.resize(rotated, (500, 500),  # type: ignore
                    interpolation=cv.INTER_CUBIC)  # type: ignore
cv.imshow("resized", resized)
# fliping
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)
flip1 = cv.flip(img, -1)
cv.imshow('Flip', flip1)
# cropping
cropped = img[200:400, 300:400]
cv.imshow("croped", cropped)
cv.waitKey(0)
cv.destroyAllWindows
