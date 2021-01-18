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





val_class1_path = 'events100_gaussianMapping/data_filtered_final/validation/mannequin'
val_class2_path = 'events100_gaussianMapping/data_filtered_final/validation/not_mannequin'

testing_class1_path = 'events100_gaussianMapping/data_filtered_final/testing/mannequin'
testing_class2_path = 'events100_gaussianMapping/data_filtered_final/testing/not_mannequin'

split_size =.5

split_data(val_class1_path,testing_class1_path,split_size)
split_data(val_class2_path,testing_class2_path,split_size)

