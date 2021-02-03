import numpy as np
import cv2
import os

def upscale_frame(src_path,des_path):
    img = os.listdir(src_path)
    n = len(img)
    upscaled_img = np.zeros((240,320))
    count = 0
    count_up = 0
    upscale_size = 2

    for i in range(n):
        temp = cv2.imread(os.path.join(src_path,str(i)+'.png'),0)
        upscaled_img += temp
        count_up += 1
        if count_up == upscale_size:
            upscaled_img = upscaled_img*255/upscaled_img.max()
            # upscaled_img = upscaled_img/upscale_size
            cv2.imwrite(os.path.join(des_path,str(count)+'.png'),upscaled_img)
            count_up = 0
            count += 1
            upscaled_img[:] = 0

    # for x in img:
    #     for i in range(10):
    #         temp = cv2.imread(os.path.join(src_path,x),0)
    #         upscaled_img += temp

    #     upscaled_img = upscaled_img*255/upscaled_img.max()
    #     # upscaled_img = upscaled_img/upscale_size
    #     cv2.imwrite(os.path.join(des_path,str(count)+'.png'),upscaled_img)
    #     count += 1
    #     upscaled_img[:] = 0



src = os.path.join(os.curdir,'EventsFrame_27012020')
src_folder = os.path.join(src,'mannequin_back')

des = os.path.join(os.curdir,'EventsFrame_27012020')
des_folder = os.path.join(des,'mannequin_back_upscaled_2')

upscale_frame(src_folder,des_folder)





