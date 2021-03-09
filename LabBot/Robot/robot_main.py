from functions import *
from circle import*


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
    
    
    if mode == 3:
        if used == 1:
            if positionRobot[0] > middleRight:
                point(pointRightMiddle
            elif positionTarget[0] < middleLeft:
                
            point(positionTarget[0],positionTarget[1],positionRobot[0],positionRobot[1],positionRobot[2])
            
        
        else:
            circle()
        
    elif mode == 2:
        
        circle()
        
    
    elif mode == 1:
        
        
        