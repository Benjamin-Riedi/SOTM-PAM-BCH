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
    
    if mode == 3:
        if used == 1:
            point(positionTarget[0],positionTarget[1],positionRobot[0],positionRobot[1],positionRobot[2])
            
            angleTarget = getAngle(positionRobot[0], positionRobot[1], positionTarget[0], positionTarget[1])
            
            
            while angleTarget - 5 > positionRobot[2]:
                rightMotor(1)
            while angleTarget + 5 < positionRobot[2]:
                leftMotor(1)
            while positionRobot[2] < angleTarget + 5 and positionRobot[2] > angleTarget - 5 and positionRobot[0] < positionTarget[0] - 5 and positionRobot[0] > positionTarget[0] + 5 and positionRobot[1] < positionTarget[1] - 5 and positionRobot[1] > positionTarget[1]:
                ultSensor = dataUlt()
                if ultSensor != 1:
                    leftMotor(1)
                    rightMotor(1)
        
        else:
            circle()
        
    elif mode == 2:
        
        circle()
        
    
    elif mode == 1:
        
        
        