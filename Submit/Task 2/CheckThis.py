#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 21:16:26 2019

@author: arka
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

left_img=cv2.imread('left_image.jpg',0)
right_img=cv2.imread('right_image.jpg',0)


x_Max=752
y_Max=480
#points of correspondance taken manually
points1=[[69,129],[27,608],[168,307],[182,453],[96,436],[97,322],[112,490],[310,472],[135,160],[176,154]]

points2=[[64,119],[18,589],[164,249],[175,391],[90,391],[91,303],[105,471],[304,453],[130,147],[171,142]]

points1=np.int32(points1)

points2=np.int32(points2)


t=points1[:,0].copy()
points1[:,0]=points1[:,1].copy()
points1[:,1]=t.copy()

t=points2[:,0].copy()
points2[:,0]=points2[:,1].copy()
points2[:,1]=t.copy()
#The fundamental 
fmat,mask=cv2.findFundamentalMat(points1,points2,cv2.FM_RANSAC,1,0.9999)
'''
points1 = points1[:,:][mask.ravel()==1]
points2 = points2[:,:][mask.ravel()==1]
'''
p1fNew = points1.reshape((points1.shape[0] * 2, 1))
p2fNew = points2.reshape((points2.shape[0] * 2, 1))
#Rectified matrixes obtained
retBool ,rectmat1, rectmat2 = cv2.stereoRectifyUncalibrated(p1fNew,p2fNew,fmat,(752,480))
norm1=rectmat1.sum()
rectmat1=rectmat1/(norm1)
norm2=rectmat2.sum()
rectmat2=rectmat2/(norm2)
left_img=np.float32(left_img)

right_img=np.float32(right_img)
left_new=cv2.filter2D(left_img,-1,rectmat1)
right_new=cv2.filter2D(right_img,-1,rectmat2)
cv2.imwrite ("new_limg.jpg",left_new)
cv2.imwrite("new_rimg.jpg",right_new)



x_Max=752
y_Max=480
fil=np.ones((3,3),dtype=float)
fil=fil/9

right_img=right_new
left_img=left_new

right_img=cv2.filter2D(right_img,-1,fil)
disparity=np.zeros((y_Max,x_Max))

n=3
z=25
#disparity map obtained
for i in range(n,x_Max-n):
    print(i)
    for j in range(n,y_Max-n):
        arr=np.int64(left_img[j-n:j+n,i-n:i+n])
        minval=256*256*n*n*4
        min_num=0
        for k1 in range(n,x_Max-n):
            if(k1-i>90):
                break
            try:
                if(abs(k1-i)>90):
                    continue
                arr2=np.int64(right_img[j-n:j+n,k1-n:k1+n])
            
                sumtot=(arr2-arr)*(arr2-arr)
                sumtot=sumtot.sum()
                if(sumtot<minval):
                    minval=sumtot
                    min_num=abs(k1-i)
            except:
                continue
        disparity[j][i]=abs(min_num)

div=np.max(disparity)
disparity2=np.uint8(disparity/div*255)
cv2.imshow("disparity",disparity2)


