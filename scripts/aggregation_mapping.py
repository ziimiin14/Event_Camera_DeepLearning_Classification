

import numpy as np


## Calculate the gradient value and store it for future use
points =np.array((150,150))
points = points.reshape(1,-1)
hor = points[0,0]
ver = points[0,1]
x = np.arange(hor-3,hor+4)
y = np.arange(ver-3,ver+4)
X,Y = np.meshgrid(x,y)
T = np.array((X.T.flatten(),Y.T.flatten()))
T = T.T
exponent=np.sum((T-points)**2,1)/(2*(1**2))
amplitude = 1/(1*np.sqrt(2*np.pi))
val = amplitude* np.exp(-exponent)
val = val.reshape(7,7)


def cal_mg(points,value=val):
    rows = 246
    cols = 326
    events_img = np.zeros((rows,cols))
    
    for i in range(points.shape[0]):

        hor = points[i,0]
        ver = points[i,1]
        

        events_img[ver:ver+7,hor:hor+7] = events_img[ver:ver+7,hor:hor+7] + value
    
    
    events_img = events_img[3:rows-3,3:cols-3]
    events_img = events_img/events_img.max()
    return events_img




# ## Convert x,y pixel into (n,2) array
# x = np.array([[0,0],[190,190],[319,239]])


# ## For each 10ms calculate the image with weight gradient and save it
# img = cal_mg(x,val)



