import cv2
import numpy as np
import matplotlib.pyplot as plt

left_img=cv2.imread('left_image.jpg',0)
right_img=cv2.imread('right_image.jpg',0)


x_Max=752
y_Max=480


disparity=np.zeros((y_Max,x_Max))
fil=np.ones((3,3),dtype=float)/9
right_img1=cv2.filter2D(right_img,-1,fil)
n=5
z=30

for i in range(n,x_Max-n):
    print(i)
    for j in range(n,y_Max-n):
        arr=np.int64(left_img[j-n:j+n,i-n:i+n])
        minval=256*256*n*n*4
        min_num=0
        for k1 in range(i-z,i+z):
            for k2 in range(j-z,j+z):
                try:
                    arr2=np.int64(right_img1[k2-n:k2+n,k1-n:k1+n])
                
                    sumtot=(arr2-arr)*(arr2-arr)
                    sumtot=sumtot.sum()
                    if(sumtot<minval):
                        minval=sumtot
                        min_num=((k2-j)**2+(k1-i)**2)**0.5
                except:
                    continue
        disparity[j][i]=abs(min_num)

            
                
            
        
        
        