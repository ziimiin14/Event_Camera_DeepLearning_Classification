import numpy as np

from google.colab import files
from keras.preprocessing import image

uploaded=files.upload()

for fn in uploaded.keys():

  # predicting images
  path='/content/' + fn
  img=image.load_img(path, target_size=(150, 150))

  x=image.img_to_array(img)
  x=np.expand_dims(x, axis=0)
  images = np.vstack([x])

  classes = model.predict(images, batch_size=10)

  print(classes[0])

  if classes[0]>0:
    print(fn + " is a dog")
    
  else:
    print(fn + " is a cat")


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