from robot_functions import *
from time import sleep
import webbrowser
import bluetooth as bt
import sys
import time
import RPi.GPIO as GPIO

left_forward=17
left_backward=27
right_forward=23
right_backward=24
sleeptime=1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(left_forward, GPIO.OUT)
GPIO.setup(left_backward, GPIO.OUT)
GPIO.setup(right_forward, GPIO.OUT)
GPIO.setup(right_backward, GPIO.OUT)

mode = 1
used = 0
positionRobot = [0,0,0]
positionTarget = [0,0]

mac = 'DC:A6:32:D0:BB:86'
port = 9
backlog = 1
size = 2048
s = bt.BluetoothSocket(bt.RFCOMM)
s.bind((mac, port))
s.listen(backlog)
client, clientInfo = s.accept()

last = 0
place = 3

transition = 0
while True:
    
    data = client.recv(size)
    btlist = data.encode()
    bluetooth = btlist.strip("[]'").split(", ")
    bluetooth = map(int, bluetooth)
    print(bluetooth, type(bluetooth))
    mode = bluetooth[6]
    used = bluetooth[5]
    positionRobot[0] = bluetooth[0]
    positionRobot[1] = bluetooth[1]
    positionRobot[2] = bluetooth[2]
    positionTarget[0] = bluetooth[3]
    positionTarget[1] = bluetooth[4]
    
    
    middleRight = 300
    middleLeft = 125
    pointRightMiddle_x = 360
    pointRightMiddle_y = 260
    pointLeftMiddle_x = 100
    pointLeftMiddle_y = 250
    transitionNeed = 0
    if mode == 3:
        if used == 1:
            last = 0
            if positionRobot[0] > middleLeft and positionTarget[0] < middleLeft:
                transitionNeed = 1
            elif positionRobot[0] < middleRight and positionTarget[0] > middleRight:
                transitionNeed = 2
            if transitionNeed == 1:
                if transition == 0:
                    finished = point(pointRightMiddle_x, pointRightMiddle_y,positionRobot[0],positionRobot[1],positionRobot[2])
                    if finished == 1:
                        transition = 1
                        finished = 0
                if transition == 1:
                    finished = point(pointLeftMiddle_x, pointLeftMiddle_y,positionRobot[0],positionRobot[1],positionRobot[2])
                    if finished == 1:
                        transitionNeed = 0
                        finished = 0
                        transition = 0
            elif transitionNeed == 2:
                if transition == 0:
                    finished = point(pointLeftMiddle_x, pointLeftMiddle_y,positionRobot[0],positionRobot[1],positionRobot[2])
                    if finished == 1:
                        transition = 1
                        finished = 0
                if transition == 1:
                    finished = point(pointRightMiddle_x, pointRightMiddle_y,positionRobot[0],positionRobot[1],positionRobot[2])
                    if finished == 1:
                        transitionNeed = 0
                        finished = 0
                        transition = 0
            else:
                finished = point(positionTarget[0], positionTarget[1],positionRobot[0],positionRobot[1],positionRobot[2])
                if finished == 1:
                    sleep(5)
                    webbrowser.open("http://10.2.42.236/LabBot_21/site3.php")
                    
                    
            
        
        else:
            if last == 0:
                if positionRobot[0] < 200:
                    place = 0
                elif positionRobot[0] > 200:
                    place = 1
            
            circle(positionRobot[0], positionRobot[1], positionRobot[2],place)
            last = 1
        
    elif mode == 2:
        if last == 0:
            if positionRobot[0] < 200:
                place = 0
            elif positionRobot[0] > 200:
                place = 1
            
        circle(positionRobot[0], positionRobot[1], positionRobot[2],place)
        last = 1
        
    
    elif mode == 1:
        last = 0
        
        
        
