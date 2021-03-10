from functions import*
import math
import numpy as np
import cv2
import time
import os
import bluetooth
serveraddr = 'DC:A6:32:0B:24:C2'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serveraddr, port))


# This system command loads the right drivers for the Raspberry Pi camera
os.system('sudo modprobe bcm2835-v4l2')

w=480
h=320

my_camera = cv2.VideoCapture(0)
my_camera.set(3,w)
my_camera.set(4,h)
time.sleep(2)

while (True):
    success, image = my_camera.read()
    image = cv2.flip(image,-1)
    image = cv2.GaussianBlur(image,(5,5),0)

    image_HSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    
    
    
    
    
    lower_pink = np.array([140,150,125])
    upper_pink = np.array([180,230,170])
    
    
    
    mask = cv2.inRange(image_HSV,lower_pink,upper_pink)
    mask = cv2.GaussianBlur(mask,(5,5),0)
    
    

    # findContours returns a list of the outlines of the white shapes in the mask (and a heirarchy that we shall ignore)            
    # API differences:
    #   OpenCV 2.x: findContours -> contours, hierarchy
    #   OpenCV 3.x: findContours -> image, contours, hierarchy
    #   OpenCV 4.x: findContours -> contours, hierarchy
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    position=[0,0,0,0]
    # If we have at least one contour, look through each one and pick the biggest
    if len(contours)>0:
        largest = 0
        area = 0
        for i in range(len(contours)):
            # get the area of the ith contour
            temp_area = cv2.contourArea(contours[i])
            # if it is the biggest we have seen, keep it
            if temp_area > area:
                area = temp_area
                largest = i
        # Compute the coordinates of the center of the largest contour
        coordinates = cv2.moments(contours[largest])
        target_x = int(coordinates['m10']/coordinates['m00'])
        target_y = int(coordinates['m01']/coordinates['m00'])
        # Pick a suitable diameter for our target (grows with the contour)
        diam = int(np.sqrt(area)/4)
        # draw on a target
        cv2.circle(image,(target_x,target_y),diam,(0,255,0),1)
        cv2.line(image,(target_x-2*diam,target_y),(target_x+2*diam,target_y),(0,255,0),1)
        cv2.line(image,(target_x,target_y-2*diam),(target_x,target_y+2*diam),(0,255,0),1)
        
        linkstisch = 0
        mittetisch = 0
        rechtstisch = 0
        anfangtisch = 0
        if target_x >= linkstisch and target_x <= mittetisch and target_y <= anfangtisch:
            target_x = 0
        if target_x <= rechtstisch and target_x >= mittetisch and target_y <= anfangtisch:
            target_x = 0
            
        position[0]=target_x
        position[1]=target_y
        
        
        
        
        
    lower_yellow = np.array([35,130,80])
    upper_yellow = np.array([50,170,130])
    
    
    
    
    mask = cv2.inRange(image_HSV,lower_yellow,upper_yellow)
    mask = cv2.GaussianBlur(mask,(5,5),0)
    
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    
    if len(contours)>0:
        largest = 0
        area = 0
        for i in range(len(contours)):
            # get the area of the ith contour
            temp_area = cv2.contourArea(contours[i])
            # if it is the biggest we have seen, keep it
            if temp_area > area:
                area = temp_area
                largest = i
        # Compute the coordinates of the center of the largest contour
        coordinates = cv2.moments(contours[largest])
        target_x = int(coordinates['m10']/coordinates['m00'])
        target_y = int(coordinates['m01']/coordinates['m00'])
        # Pick a suitable diameter for our target (grows with the contour)
        diam = int(np.sqrt(area)/4)
        # draw on a target
        cv2.circle(image,(target_x,target_y),diam,(0,255,0),1)
        cv2.line(image,(target_x-2*diam,target_y),(target_x+2*diam,target_y),(0,255,0),1)
        cv2.line(image,(target_x,target_y-2*diam),(target_x,target_y+2*diam),(0,255,0),1)
        position[2]=target_x
        position[3]=target_y
        
        
        
        
        
    lower_green = np.array([35,130,80])
    upper_green = np.array([50,170,130])
    
    
    
    
    
    mask = cv2.inRange(image_HSV,lower_green,upper_green)
    mask = cv2.GaussianBlur(mask,(5,5),0)
    
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    positionrobot=[0,0,0,0,0]
    if len(contours)>0:
        largest = 0
        area = 0
        for i in range(len(contours)):
            # get the area of the ith contour
            temp_area = cv2.contourArea(contours[i])
            # if it is the biggest we have seen, keep it
            if temp_area > area:
                area = temp_area
                largest = i
        # Compute the coordinates of the center of the largest contour
        coordinates = cv2.moments(contours[largest])
        target_x = int(coordinates['m10']/coordinates['m00'])
        target_y = int(coordinates['m01']/coordinates['m00'])
        # Pick a suitable diameter for our target (grows with the contour)
        diam = int(np.sqrt(area)/4)
        # draw on a target
        cv2.circle(image,(target_x,target_y),diam,(0,255,0),1)
        cv2.line(image,(target_x-2*diam,target_y),(target_x+2*diam,target_y),(0,255,0),1)
        cv2.line(image,(target_x,target_y-2*diam),(target_x,target_y+2*diam),(0,255,0),1)
        linkstisch = ?
        mittetisch = ?
        rechtstisch = ?
        anfangtisch = ?
        if target_x >= linkstisch and target_x <= mittetisch and target_y <= anfangtisch:
            target_x = ?
        if target_x <= rechtstisch and target_x >= mittetisch and target_y <= anfangtisch:
            target_x = ?
        
        
        
        positionrobot[3]=target_x
        positionrobot[4]=target_y
    cv2.imshow('View',image)
    
    positionrobot[0]=position[0]+((position[2]-position[0])/2)
    positionrobot[1]=position[1]+((position[3]-position[1])/2)
    if (position[0]-positionrobot[0])== 0 and (position[1]-positionrobot[1])<=0:
        positionrobot[2] = 270
    elif (position[0]-positionrobot[0])== 0 and (position[1]-positionrobot[1])>=0:
        positionrobot[2] = 90
    else:
        positionrobot[2] = math.degrees(math.atan((position[1]-positionrobot[1])/(position[0]-positionrobot[0])))
        if (position[0]-positionrobot[0])<=0:
            positionrobot[2] = positionrobot[2] +180
        elif (position[1]-positionrobot[1])<=0 and (position[0]-positionrobot[0])>=0:
            positionrobot[2] = positionrobot[2]+360
    position2 = positionrobot+ordersCheck()+modeCheck()
    print(time.strftime(" %H: %M: %S:"))
    
    
    
    
    s.send(position2)
    print(position2)
    
    
    
    
    
    
 # Esc key to stop, otherwise repeat after 3 milliseconds   positionTarget()+
    key_pressed = cv2.waitKey(3)
    if key_pressed == 27:    
        break
    
    
cv2.destroyAllWindows()
my_camera.release()
# due to a bug in openCV you need to call wantKey three times to get the
# window to dissappear properly. Each wait only last 10 milliseconds
cv2.waitKey(10)
time.sleep(0.1)
cv2.waitKey(10)
cv2.waitKey(10)