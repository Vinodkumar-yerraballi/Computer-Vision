from cProfile import label
from cgi import print_environ
import os
import cv2 as cv
import numpy as np

DIR = '/home/vinod/Downloads/Image_classification'
people = ['Iron_Man', 'chris', 'Been', 'Messi', 'Jonny', 'Vijay', 'CR7']
haar_cassed = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
features = []
labels = []
# create a fuction for traindef create_train():


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cassed.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)  # type: ignore
                labels.append(label)  # type: ignore


create_train()

print('Training done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)


print(f'Length of the feature={len(features)}')
print(f'Length of the labels={len(labels)}')

# facerecogizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)
np.save('features.npy', features)
np.save('labels.npy', labels)
face_recognizer.save('face_trained.yml')
