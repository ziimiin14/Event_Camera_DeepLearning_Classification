import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import os

image_size = 224
def read_and_prep_images(img_paths, img_height=image_size, img_width=image_size):
    imgs = [load_img(img_path, target_size=(img_height, img_width)) for img_path in img_paths]
    img_array = np.array([img_to_array(img) for img in imgs])
    #output = img_array
    output = preprocess_input(img_array)
    return(output)

a = [os.path.join('./mannequin_filter',filename) for filename in os.listdir('./mannequin_filter')]


x = read_and_prep_images(a)
# x = (x-x.min())/(x.max()-x.min())
# print(x.min())
# print(x.max())