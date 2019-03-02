#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:55:07 2019

@author: arka
"""

import cv2
import cv2.cv as cv

def cut(disparity, image, threshold):
 for i in range(0, image.height):
  for j in range(0, image.width):
   # keep closer object
   if cv.GetReal2D(disparity,i,j) > threshold:
    cv.Set2D(disparity,i,j,cv.Get2D(image,i,j))

# loading the stereo pair
left  = cv.LoadImage('scene_l.bmp',cv.CV_LOAD_IMAGE_GRAYSCALE)
right = cv.LoadImage('scene_r.bmp',cv.CV_LOAD_IMAGE_GRAYSCALE)

disparity_left  = cv.CreateMat(left.height, left.width, cv.CV_16S)
disparity_right = cv.CreateMat(left.height, left.width, cv.CV_16S)

# data structure initialization
state = cv.CreateStereoGCState(16,2)
# running the graph-cut algorithm
cv.FindStereoCorrespondenceGC(left,right,
                          disparity_left,disparity_right,state)

disp_left_visual = cv.CreateMat(left.height, left.width, cv.CV_8U)
cv.ConvertScale( disparity_left, disp_left_visual, -16 );
cv.Save( "disparity.pgm", disp_left_visual ); # save the map

# cutting the object farthest of a threshold (120)
cut(disp_left_visual,left,120)

cv.NamedWindow('Disparity map', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Disparity map', disp_left_visual)
cv.WaitKey()