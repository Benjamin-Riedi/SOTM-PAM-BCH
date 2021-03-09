import math

def circle(positionRobot_x, positionRobot_y, angleRobot):
    angleTarget = getAngle(positionRobot_x, positionRobot_y, positionTarget_x, positionTarget_y)
    if circle == 1:
        
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
    
    angleTarget = getAngle(positionRobot_x, positionRobot_y, positionTarget_x, positionTarget_y)
    
        
    
    if angleTarget - 5 > angleRobot:
        rightMotor(1)
        #angleTarget = getAngle(positionRobot_x, positionRobot_y, positionTarget_x, positionTarget_y)
    if angleTarget + 5 < angleRobot:
        leftMotor(1)
        #angleTarget = getAngle(positionRobot_x, positionRobot_y, positionTarget_x, positionTarget_y)
    if (positionRobot_x < positionTarget_x - 5 or positionRobot_x > positionTarget_x + 5) and (positionRobot_y < positionTarget_y - 5 or positionRobot_y > positionTarget_y + 5):
        ultSensor = dataUlt()
        if ultSensor != 1:
            leftMotor(1)
            rightMotor(1)
        #angleTarget = getAngle(positionRobot_x, positionRobot_y, positionTarget_x, positionTarget_y)
    else:
        finished = 1
        return finished
    
    
    
    
#trasnition Points
#What if at Target