import os
import random
from shutil import copyfile, move

def split_data(src,training,testing,split_size):
    img = os.listdir(src)
    random.sample(img,len(img))
    random.sample(img,len(img))
    random.sample(img,len(img))

    train_img =img[0:int(split_size*len(img))]
    test_img = img[int(split_size * len(img)):]


    for x in train_img:
        temp = os.path.join(src,x)
        temp1 = os.path.join(training,x)
        copyfile(temp,temp1)
        # move(temp,temp1)

    for y in test_img:
        temp = os.path.join(src, y)
        temp1 = os.path.join(testing, y)
        copyfile(temp,temp1)
        # move(temp, temp1)





src_cat = 'eventsData/training/mannequin'
src_dog = 'eventsData/training/not_mannequin'

training_cat_path = 'eventsData_train/mannequin'
training_dog_path = 'eventsData_train/not_mannequin'

testing_cat_path = 'eventsData_val/mannequin'
testing_dog_path = 'eventsData_val/not_mannequin'

split_size =.8

split_data(src_cat,training_cat_path,testing_cat_path,split_size)
split_data(src_dog,training_dog_path,testing_dog_path,split_size)

