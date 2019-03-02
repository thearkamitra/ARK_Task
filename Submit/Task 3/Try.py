#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 01:42:28 2019

@author: arka
"""

#import maze.py
import os
import cv2
import pyautogui
import time
import numpy as np
print("Press y to give inputs on your own.")
k=raw_input()
os.system("python2 maze.py &")

##To be used when the points are not known
if(k=='y'):
	print("Please Click on the left top and bottom down corners before starting. Bring the mouse pointer on the border and press anything. Do this twice")


	k=raw_input()
	c,a=pyautogui.position()
	k=raw_input()
	d,b=pyautogui.position()
	print(a,b,c,d)
else:
	a,b,c,d=326, 1070, 8, 1358
#time.sleep(5)
def crop(image,a=a,b=b,c=c,d=d):
	return image[a:b,c:d]


def seearound():#sees the brightest position and goes towards it
	#L=[]
	best=0
	best_bright1=0
	for i in range(7):

		pyautogui.keyDown('d')
		time.sleep(0.8)
		pyautogui.keyUp('d')

		image=pyautogui.screenshot()
		image=np.uint8(image)
		image=crop(image)
		image=image[:,:,::-1]
		#L.append(image)
		image2=image[350,:,1]
		brightest=np.max(image2)
		if (brightest>=best_bright1):
			best_bright1=brightest
			best=i
			print(best)

	print("The best is")
	print(best)
	for j in range(6-best):

		pyautogui.keyDown('a')
		time.sleep(0.8)
		pyautogui.keyUp('a')



		#cv2.imwrite("screenshot"+str(i)+".jpg",image)
		
	return best_bright1



best_bright=0

while(1):
	seearound()
	print("Start")
	#goes forward
	pyautogui.keyDown("w")
	time.sleep(1)
	pyautogui.keyUp("w")
	#to check if it is stranded
	t=0
	flag=0
	image=pyautogui.screenshot()
	image=np.uint8(image)
	image=crop(image)
	x=int(len(image[0])/2)
	sand_search=image[700,:,2]

	if(sand_search[x]>=100):#sand is there and t=1 means we go right
		for i in range(x-1):
			if(sand_search[x+i]<=100):
				t=2
			elif(sand_search[x-i]<=100):
				t=1
			if(t!=0):
				break
	else:
		for i in range(x-1):
			if(sand_search[x+i]>=100):
				t=1
			elif(sand_search[x-i]<=100):
				t=2
			if(t!=0):
				break
		if(t==0):#there is no sand at all

			pyautogui.keyDown('s')
			time.sleep(0.4)
			pyautogui.keyUp('s')
			if(np.random.randint(2)):

				pyautogui.keyDown(',')
				time.sleep(0.4)
				pyautogui.keyUp(',')
			else:

				pyautogui.keyDown('.')
				time.sleep(0.4)
				pyautogui.keyUp('.')





	# for i in range(len(sand_search)/2):
	# 	if(sand_search[i]<=100):
	# 		t+=1
	# 	if(sand_search[len(sand_search)-i-1]<=100):
	# 		t+=10000
	# 	if(t!=0):
	# 		flag+=1
	# 	if(flag==200):
	# 		continue
	# if(t>10000 and t%10000>0):
	# 	print("Overall stuck")

	# 	pyautogui.keyDown('s')
	# 	time.sleep(0.4)
	# 	pyautogui.keyUp('s')
	# 	if(np.random.randint(2)):

	# 		pyautogui.keyDown(',')
	# 		time.sleep(0.4)
	# 		pyautogui.keyUp(',')
	# 	else:

	# 		pyautogui.keyDown('.')
	# 		time.sleep(0.4)
	# 		pyautogui.keyUp('.')
	# 	continue


	if(t==1):
		print("left stuck")

		pyautogui.keyDown(',')
		time.sleep(0.4)
		pyautogui.keyUp(',')
		continue
	if(t==2):

		print("right stuck")
		pyautogui.keyDown('.')
		time.sleep(0.4)
		pyautogui.keyUp('.')
		continue

'''
	pyautogui.keyDown("d")
	pyautogui.keyDown("w")
	
	time.sleep(0.9)

	pyautogui.keyUp("w")
	pyautogui.keyUp("d")

	pyautogui.keyDown("w")
	time.sleep(1)
	pyautogui.keyUp("w")
'''
'''
'''
'''
	pyautogui.keyDown("a")
	time.sleep(0.9)
	pyautogui.keyUp("a")


	pyautogui.keyDown("w")
	time.sleep(1)
	pyautogui.keyUp("w")

	pyautogui.keyDown("d")
	time.sleep(0.9)
	pyautogui.keyUp("d")

	pyautogui.keyDown("w")
	time.sleep(1)
	pyautogui.keyUp("w")
'''

'''
if(best_bright2==best_bright):
	pyautogui.keyDown("s")
	time.sleep(2)
	pyautogui.keyUp("s")
	pyautogui.keyDown("d")
	time.sleep(2)
	pyautogui.keyUp("d")
	pyautogui.keyDown("w")
	time.sleep(1)
	pyautogui.keyUp("w")
else:
	best_bright=best_bright2
	pyautogui.keyDown("w")
	time.sleep(4)
	pyautogui.keyUp("w")
'''