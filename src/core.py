import numpy as np
from keras.applications import VGG19
from keras.applications.vgg19 import preprocess_input
from keras.engine import Model
from keras.preprocessing import image


def load_image_to_vector():
    base_model = VGG19(weights='imagenet')
    model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)

    def image_to_vector(image_path):
        img = image.load_img(image_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        pred = model.predict(x)
        return pred.ravel()

    return image_to_vector


image_to_vector_process = load_image_to_vector()
