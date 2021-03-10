from functions import *
from circle import*
from time import sleep

transition = 0
while True:
    mode = bluetooth[5]
    used = bluetooth[6]
    positionRobot[0] = bluetooth[0]
    positionRobot[1] = bluetooth[1]
    positionRobot[2] = bluetooth[2]
    positionTarget[0] = bluetooth[3]
    positionTarget[1] = bluetooth[4]
    
    point(positionTarget[0],positionTarget[1],positionRobot[0],positionRobot[1],positionRobot[2])
    
    middleRight = 300
    middleLeft = 200
    pointRightMiddle_x =
    pointRightMiddle_y =
    pointLeftMiddle_x =
    pointLeftMiddle_y =
    if mode == 3:
        if used == 1:
            if positionRobot[0] > middleLeft and positionTarget[0] < middleLeft:
                transitionNeed = 1
            elif positionRobot[0] < middleRight and positionTarget[0] > middleRight:
                transitionNeed = 2
            if transitionNeed == 1
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
            elif:
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
                    
            
        
        else:
            circle()
        
    elif mode == 2:
        
        circle()
    
    elif mode == 1:
        
        
        