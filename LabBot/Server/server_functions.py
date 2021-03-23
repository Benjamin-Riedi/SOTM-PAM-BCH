import numpy as np
import cv2
import time
import os
import math 

#Function positionAim() finished

def ordersCheck():
    usedDatei = open("/var/www/LabBot_21/used.txt", "r")
    used=[0]
    used[0] = usedDatei.read()
    return used[0]

def modeCheck():
    modeDatei = open("/var/www/LabBot_21/mode.txt", "r")
    mode=[0]
    mode[0] = modeDatei.read()
    return mode[0]
    
