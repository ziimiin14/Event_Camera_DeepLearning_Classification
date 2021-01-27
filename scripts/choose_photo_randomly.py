import os
import random
from shutil import copyfile, move

def random_choose_img(src,des,length):
    count = 0
    for y in src:    
        img = os.listdir(y)
        for i in range(10):
            random.sample(img,len(img))

        img_random =img[0:length*5:5]

        for x in img_random:
            temp = os.path.join(y,x)
            temp1 = os.path.join(des,str(count)+'.png')
            count += 1
            copyfile(temp,temp1)
            # move(temp,temp1)




src = ['EventsFrame_19012020/upscaled_data/upscaled2_synthetic_event_frame_1/mannequin/mannequin_front','EventsFrame_19012020/upscaled_data/upscaled2_synthetic_event_frame_1/mannequin/mannequin_side']

des = 'EventsFrame_19012020/random_chosen_img'

random_choose_img(src,des,150)
