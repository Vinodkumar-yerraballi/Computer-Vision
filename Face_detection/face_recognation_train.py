import os
import cv2 as cv
import numpy as np
from regex import P

people = ['Iron_Man', 'chris', 'Been', 'Messi', 'Jonny', 'Vijay', 'CR7']
p = []
for i in os.listdir(r'/home/vinod/Downloads/Image_classification/test_path'):
    p.append(i)
print(p)
