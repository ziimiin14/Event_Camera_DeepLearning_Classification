import os
import random
from shutil import copyfile, move

def random_choose_img(src,des,length):
    count = 0
    for y in src:    
        img = os.listdir(y)
        for i in range(37):
            random.sample(img,len(img))

        img_random =img[0:length*5:5]

        for x in img_random:
            temp = os.path.join(y,x)
            temp1 = os.path.join(des,str(count)+'.png')
            count += 1
            copyfile(temp,temp1)
            # move(temp,temp1)




# src = ['EventsFrame_19012020/upscaled_data/upscaled2_synthetic_event_frame_1/mannequin/mannequin_front','EventsFrame_19012020/upscaled_data/upscaled2_synthetic_event_frame_1/mannequin/mannequin_side']

src = ['ReconstructedFrame_15022021/raw_data/data_mannequin_backfar/reconstruction',
'ReconstructedFrame_15022021/raw_data/data_mannequin_backnear/reconstruction',
'ReconstructedFrame_15022021/raw_data/data_mannequin_frontfar/reconstruction',
'ReconstructedFrame_15022021/raw_data/data_mannequin_frontnear/reconstruction',
'ReconstructedFrame_15022021/raw_data/data_mannequin_sidefar_1/reconstruction',
'ReconstructedFrame_15022021/raw_data/data_mannequin_sidenear_1/reconstruction',
'ReconstructedFrame_15022021/raw_data/data_mannequin_sidefar_2/reconstruction',
'ReconstructedFrame_15022021/raw_data/data_mannequin_sidenear_2/reconstruction']

des = 'ReconstructedFrame_15022021/randomly_chosen_data'

random_choose_img(src,des,50)
