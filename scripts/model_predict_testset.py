import numpy as np

from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

model = load_model('kratos_event_cam_project/scripts/ResNet50V2_softmax_Synthetic_Upscale_Frame.h5')
path = './test_mannequin/4384.png'
img = load_img(path,target_size=(64,64))
img = img_to_array(img)
img = img/255
img = np.expand_dims(img,axis = 0)
result = model.predict(img)
print(result)

# import tensorflow as tf
# from tensorflow.keras.preprocessing import image
# import numpy as np

# model = tf.keras.models.load_model('dog_cat_full.h5')

# img = image.load_img('../../../Downloads/cat1.jpeg',target_size=(150,150))

# x = image.img_to_array(img)
# x = np.expand_dims(x,axis=0)
# images = np.vstack([x])

# classes = model.predict(images,batch_size=10)

# print(classes[0])
# # > 0 = dog
# # else = cat