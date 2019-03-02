import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import time
#Parameters
biasing=20
vel=6

#The values the given figure has
max_X=1080
max_Y=1920#imge destription
source_x=932
source_y=560#source and destination
count=0
final_x=342
final_y=1402


cap=cv2.VideoCapture("dynamic_obstacles.mp4")
#Stores the list of nodes
NodeList=[]
ParentList=[]#Stores the list of parent nodes
Stopped=[]#Stoes whether the path is blocked or not
NodeList.append([source_x,source_y,0])
ParentList.append([-1,0,0])
Stopped.append(0)
Reached=False#Has it reached? I dont think so

runs=0
ret=True
count=0
sec=0
t1=time.time()
while(not Reached):#Will run till the Particle Reaches position
	if(count==0):#or abs(time.time()-t1)>=sec):
		#try:#Incase of error, 
		ret,image=cap.read()
		if(ret):
			image2=image.copy()
		#except:
		image=image2.copy()
		image2=image.copy()
		sec +=1
		for i in range(1,len(NodeList)):
			if image[NodeList[i][0],NodeList[i][1]][2]<=120:#checks the values
				Stopped[i]=1#1 if it blocked
			else:
				Stopped[i]=0
		for i in range(1,len(NodeList)):
			if(Stopped[ParentList[i][2]]==1):
				Stopped[i]=1

	count=(count+1)%5
	if (random.randint(0,100)>biasing):#Biasing for more exploitation
		point=[random.randint(0,max_X),random.randint(0,max_Y)]
	else:
		point=[final_x,final_y]
	nearest=[0,0]
	minimum=(point[0]*point[0]+point[1]*point[1])
	#for i in NodeList:
	#	print(i)
	for i in NodeList:
		if(Stopped[i[2]]==1):
			continue
		dist=(i[0]-point[0])**2+(i[1]-point[1])**2
		if dist<minimum:
			nearest=i.copy()
			minimum=dist

	theta=np.arctan2(point[1]-nearest[1],point[0]-nearest[0])#finding a node
	NewNode=[0,0]
	NewNode[0]=nearest[0] + int(vel*np.cos(theta))
	NewNode[1]=nearest[1] + int(vel*np.sin(theta))
	if(NewNode[0]>max_X or NewNode[1]>max_Y or NewNode[0]<0 or NewNode[1]<0):
		continue
	if(image[NewNode[0],NewNode[1],0]<=20 and image[NewNode[0],NewNode[1],1]<=20 and image[NewNode[0],NewNode[1],2]<=20):
		continue
	if(image[NewNode[0],NewNode[1]][0]>=20 and image[NewNode[0],NewNode[1]][1]<=20 and image[NewNode[0],NewNode[1]][2]<=20):
		NodeList.append([NewNode[0],NewNode[1],len(NodeList)])
		ParentList.append([nearest[0],nearest[1],nearest[2]])
		Stopped.append(1)
		continue
	
	if(image[NewNode[0],NewNode[1]][0]<=20 and image[NewNode[0],NewNode[1]][1]>=20 and image[NewNode[0],NewNode[1]][2]<=20):			
		NodeList.append([NewNode[0],NewNode[1],len(NodeList)])
		ParentList.append([nearest[0],nearest[1],nearest[2]])
		Stopped.append(0)
		Reached=True
		print("yaa")
	NodeList.append([NewNode[0],NewNode[1],len(NodeList)])
	ParentList.append([nearest[0],nearest[1],nearest[2]])
	Stopped.append(0)


	print(runs)
	runs +=1
	if(count==0):
		for Node in NodeList:
			image2[Node[0]-1,Node[1]-1]=(255,0,0)
			image2[Node[0]-1,Node[1]]=(255,0,0)
			image2[Node[0]-1,Node[1]+1]=(255,0,0)
			image2[Node[0],Node[1]]=(255,0,0)
			image2[Node[0]+1,Node[1]-1]=(255,0,0)
			image2[Node[0]+1,Node[1]]=(255,0,0)
			image2[Node[0]+1,Node[1]+1]=(255,0,0)
	
	image2[NewNode[0]-1,NewNode[1]-1]=(255,0,0)
	image2[NewNode[0]-1,NewNode[1]]=(255,0,0)
	image2[NewNode[0]-1,NewNode[1]+1]=(255,0,0)
	image2[NewNode[0],NewNode[1]]=(255,0,0)
	image2[NewNode[0]+1,NewNode[1]-1]=(255,0,0)
	image2[NewNode[0]+1,NewNode[1]]=(255,0,0)
	image2[NewNode[0]+1,NewNode[1]+1]=(255,0,0)

	cv2.imshow("ImageD",image2)
	cv2.waitKey(1)
	









for Node in NodeList:#final colouring
	if(Stopped[Node[2]]==0):
		image2[Node[0]-1,Node[1]-1]=(255,0,0)
		image2[Node[0]-1,Node[1]]=(255,0,0)
		image2[Node[0]-1,Node[1]+1]=(255,0,0)
		image2[Node[0],Node[1]]=(255,0,0)
		image2[Node[0]+1,Node[1]-1]=(255,0,0)
		image2[Node[0]+1,Node[1]]=(255,0,0)
		image2[Node[0]+1,Node[1]+1]=(255,0,0)
	else:
		image2[Node[0]-1,Node[1]-1]=(255,0,255)
		image2[Node[0]-1,Node[1]]=(255,0,255)
		image2[Node[0]-1,Node[1]+1]=(255,0,255)
		image2[Node[0],Node[1]]=(255,0,255)
		image2[Node[0]+1,Node[1]-1]=(255,0,255)
		image2[Node[0]+1,Node[1]]=(255,0,255)
		image2[Node[0]+1,Node[1]+1]=(255,0,255)

nodeno=len(NodeList)-1
while(nodeno!=0):
	Node=NodeList[nodeno].copy()

	image2[Node[0]-1,Node[1]-1]=(255,255,255)
	image2[Node[0]-1,Node[1]]=(0,255,255)
	image2[Node[0]-1,Node[1]+1]=(0,255,255)
	image2[Node[0],Node[1]]=(0,255,255)
	image2[Node[0]+1,Node[1]-1]=(0,255,255)
	image2[Node[0]+1,Node[1]]=(0,255,255)
	image2[Node[0]+1,Node[1]+1]=(0,255,255)
	for i in range(len(NodeList)):
		if (NodeList[i]==ParentList[nodeno]):
			#print(NodeList[nodeno],ParentList[nodeno])
			nodeno=i
			break



cv2.imshow("ImageD",image2)
cv2.waitKey(0)
#image[source_x][source_y][1]=0
#image[source_x][source_y][2]=0

cap.release()
cv2.destroyAllWindows()
