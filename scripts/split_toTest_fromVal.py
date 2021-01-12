import os
import random
from shutil import copyfile, move

def split_data(val,test,split_size):
    img = os.listdir(val)
    random.sample(img,len(img))
    random.sample(img,len(img))
    random.sample(img,len(img))

    val_img =img[0:int(split_size*len(img))]
    test_img = img[int(split_size * len(img)):]


    # for x in train_img:
    #     temp = os.path.join(src,x)
    #     temp1 = os.path.join(training,x)
    #     copyfile(temp,temp1)
        # move(temp,temp1)

    for y in test_img:
        temp = os.path.join(val, y)
        temp1 = os.path.join(test, y)
        # copyfile(temp,temp1)
        move(temp, temp1)





val_cat_path = 'eventsData_val/mannequin'
val_dog_path = 'eventsData_val/not_mannequin'

testing_cat_path = 'eventsData_test/mannequin'
testing_dog_path = 'eventsData_test/not_mannequin'

split_size =.5

split_data(val_cat_path,testing_cat_path,split_size)
split_data(val_dog_path,testing_dog_path,split_size)

