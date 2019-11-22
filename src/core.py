import cv2
import tensorflow as tf


def resize_image(image_path, size):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    return cv2.resize(image, size, interpolation=cv2.INTER_AREA)


def image2vector(image_path):
    resized = resize_image(image_path, size=(224, 224))
    return tf.keras.preprocessing.image.img_to_array(img=resized).tolist()
