import os
from shutil import copyfile

des_path = os.path.join(os.curdir,'mannequin_filter')

if os.path.exists(des_path):
    pass
else:
    os.mkdir(des_path)

src_path = os.path.join(os.curdir,'mannequin')
src_path1 = os.path.join(os.curdir,'mannequin1')


images_name = os.listdir(src_path)
images_name1 = os.listdir(src_path1)

count = 0

for x in images_name:
    src_temp = os.path.join(src_path,x)
    des_temp = os.path.join(des_path,str(count)+'.jpg')
    count += 1
    copyfile(src_temp,des_temp)
    # print(des_temp)

for y in images_name1:
    src_temp1 = os.path.join(src_path1,y)
    des_temp1 = os.path.join(des_path,str(count)+'.jpg')
    count += 1
    copyfile(src_temp1,des_temp1)
    # print(des_temp1)



