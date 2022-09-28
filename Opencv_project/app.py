import re
from matplotlib import image
from matplotlib.pyplot import gray
import streamlit as st
import cv2 as cv
import numpy as np
from PIL import Image


def blank_img(img, amount):
    img_red = np.zeros(img.shape[:2], dtype='uint8')
    return img_red


def brighten_image(image, amount):
    img_bright = cv.convertScaleAbs(image, beta=amount)
    return img_bright


def blur_image(image, amount):
    blur_img = cv.GaussianBlur(image, (11, 11), amount)
    return blur_img


def enhance_details(img):
    hdr = cv.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr


def covert_gray(img, amount):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray


def covert_rgb(img, amount):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return rgb


def thresh(img, amount):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    threshold = cv.adaptiveThreshold(
        gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
    return threshold
# cut the face identifys the image


def face_rectangel(img, amount):
    haar_cassed = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_ret = haar_cassed.detectMultiScale(
        img, scaleFactor=1.1, minNeighbors=1)
    for (x, y, w, h) in face_ret:
        rectangle = cv.rectangle(
            img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        return rectangle


def main():
    st.title("OpenCV Demo App")
    st.subheader("This app allows you to play with Image filters!")
    st.text("We use OpenCV and Streamlit for this demo")

    blur_rate = st.sidebar.slider("Blurring", min_value=0.5, max_value=3.5)
    brightness_amount = st.sidebar.slider(
        "Brightness", min_value=-50, max_value=50, value=0)
    apply_enhancement_filter = st.sidebar.checkbox('Enhance Details')
    gray = st.sidebar.checkbox("gray")
    threshold_state = st.sidebar.slider(
        "threshold", min_value=0, max_value=500, value=0)
    image_rgb = st.sidebar.checkbox("RGB")
    rectangle = st.sidebar.checkbox("Face cut")
    image_file = st.file_uploader(
        "Upload Your Image", type=['jpg', 'png', 'jpeg'])
    if not image_file:
        return None

    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    processed_image = blur_image(original_image, blur_rate)
    processed_image = brighten_image(processed_image, brightness_amount)
    gray_image = covert_gray(processed_image, gray)  # type: ignore
    thresh_image = thresh(processed_image, threshold_state)
    img_rgb = covert_rgb(processed_image, image_rgb)
    cut_img = face_rectangel(processed_image, rectangle)  # type: ignore
    if apply_enhancement_filter:
        processed_image = enhance_details(processed_image)
    st.text("Original Image vs Processed Image")
    st.image([original_image, processed_image,
             gray_image, thresh_image, img_rgb, cut_img])  # type: ignore


if __name__ == '__main__':
    main()
