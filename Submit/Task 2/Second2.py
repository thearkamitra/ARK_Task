#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 02:29:00 2019

@author: arka
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from tempfile import TemporaryFile
outfile=TemporaryFile()
left_img=cv2.imread('new_limg.jpg',0)
right_img=cv2.imread('new_rimg.jpg',0)


x_Max=752
y_Max=480
fil=np.ones((3,3),dtype=float)
fil=fil/9

right_img=cv2.filter2D(right_img,-1,fil)
disparity=np.zeros((y_Max,x_Max))

n=3
z=25

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


np.save(outfile,disparity)
            
                
            
        
        
        