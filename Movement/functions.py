import math

def circle():
    #circle Function
    
    
def angleTarget(xRobot, yRobot, xTarget, yTarget):
    if (xTarget-xRobot)== 0 and (yTarget-yRobot)<=0:
        angle = 270
    elif (xTarget-xRobot)== 0 and (yTarget-yRobot)>=0:
        angle = 90
    else:
        angle = math.degrees(math.atan((yTarget-yRobot)/(xTarget-xRobot)))
        if (xTarget-xRobot)<=0:
            angle = angle +180
        elif (yTarget-yRobot)<=0 and (xTarget-xRobot)>=0:
            angle = angle+360
    return angle

def rightMotor():
    #right Motor on
    
    
def leftMotor():
    
    
def dataUlt():
    
def point(positionTarget_x, positionTarget_y, positionRobot_x, positionRobot_y, angleRobot):
    
    
    
    
