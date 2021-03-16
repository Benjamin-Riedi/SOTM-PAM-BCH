import math

def circle(positionRobot_x, positionRobot_y, angleRobot):
    angleTarget = getAngle(positionRobot_x, positionRobot_y, positionTarget_x, positionTarget_y)
    point1_x = 340
    point1_y = 82
    point2_x = 315
    point2_y = 260
    point3_x = 100
    point3_y = 250
    point4_x = 90
    point4_y = 50
    point5_x = 45
    point5_y = 235
    point6_x = 375
    point6_y = 220
    if circle == 0:
        finished = point(point1_x, point1_y,positionRobot[0],positionRobot[1],positionRobot[2])
        if finished == 1:
            circle = 1
            finished = 0
    elif circle == 1:
        finished = point(point2_x, point2_y,positionRobot[0],positionRobot[1],positionRobot[2])
        if finished == 1:
            circle = 2
            finished = 0
    elif circle == 2:
        finished = point(point3_x, point3_y,positionRobot[0],positionRobot[1],positionRobot[2])
        if finished == 1:
            circle = 3
            finished = 0
    elif circle == 3:
        finished = point(point4_x, point4_y,positionRobot[0],positionRobot[1],positionRobot[2])
        if finished == 1:
            circle = 4
            finished = 0
    elif circle == 4:
        finished = point(point5_x, point5_y,positionRobot[0],positionRobot[1],positionRobot[2])
        if finished == 1:
            circle = 5
            finished = 0
    elif circle == 5:
        finished = point(point6_x, point6_y,positionRobot[0],positionRobot[1],positionRobot[2])
        if finished == 1:
            circle = 0
            finished = 0
    
        
    #circle Function
    
    
def getAngle(xRobot, yRobot, xTarget, yTarget):
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
    
def volume():
    
    

def point(positionTarget_x, positionTarget_y, positionRobot_x, positionRobot_y, angleRobot):
    
    angleTarget = getAngle(positionRobot_x, positionRobot_y, positionTarget_x, positionTarget_y)
    
    
    
    if angleTarget - 5 > angleRobot:
        ultSensor = dataUlt()
        if ultSensor != 1:
            rightMotor(1)
            leftMotor(0)
        else:
            leftMotor(0)
            rightMotor(0)
        finished = 0
        #angleTarget = getAngle(positionRobot_x, positionRobot_y, positionTarget_x, positionTarget_y)
    elif angleTarget + 5 < angleRobot:
        ultSensor = dataUlt()
        if ultSensor != 1:
            leftMotor(1)
            rightMotor(0)
        else:
            leftMotor(0)
            rightMotor(0)
        finished = 0
        #angleTarget = getAngle(positionRobot_x, positionRobot_y, positionTarget_x, positionTarget_y)
    elif (positionRobot_x < positionTarget_x - 5 or positionRobot_x > positionTarget_x + 5) and (positionRobot_y < positionTarget_y - 5 or positionRobot_y > positionTarget_y + 5):
        ultSensor = dataUlt()
        if ultSensor != 1:
            leftMotor(1)
            rightMotor(1)
        else:
            leftMotor(0)
            rightMotor(0)
        finished = 0
        #angleTarget = getAngle(positionRobot_x, positionRobot_y, positionTarget_x, positionTarget_y)
    else:
        finished = 1
    return finished
    
    
    
    
#trasnition Points
#What if at Target