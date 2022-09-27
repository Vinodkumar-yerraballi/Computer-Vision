from cProfile import label
import cv2 as cv
import numpy as np
from setuptools import PEP420PackageFinder

haar_cassed = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
people = ['Iron_Man', 'chris', 'Been', 'Messi', 'Jonny', 'Vijay', 'CR7']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
img = cv.imread(
    r'/home/vinod/Downloads/Image_classification/test_path/Messi/images (31).jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("image", img)
face_reet = haar_cassed.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
for (x, y, w, h) in face_reet:
    face_img = gray[x:x+h, y:y+h]
    label, confidence = face_recognizer.predict(face_img)
    print(f'Label={people[label]} with confidence of {confidence}')
    cv.putText(img, str(people[label]), (20, 20),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('Deteced face', img)
cv.waitKey(0)
