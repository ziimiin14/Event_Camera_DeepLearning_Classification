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





src_class1 = 'events100_gaussianMapping/data_filtered/mannequin'
src_class2 = 'events100_gaussianMapping/data_filtered/not_mannequin'

training_class1_path = 'events100_gaussianMapping/data_filtered_final/training/mannequin'
training_class2_path = 'events100_gaussianMapping/data_filtered_final/training/not_mannequin'

testing_class1_path = 'events100_gaussianMapping/data_filtered_final/validation/mannequin'
testing_class2_path = 'events100_gaussianMapping/data_filtered_final/validation/not_mannequin'

split_size =.6

split_data(src_class1,training_class1_path,testing_class1_path,split_size)
split_data(src_class2,training_class2_path,testing_class2_path,split_size)

