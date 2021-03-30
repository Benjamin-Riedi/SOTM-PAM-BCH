# import RPi.GPIO as GPIO
# import sys
# import time
# 
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# 
# GPIO.setup(16, GPIO.OUT)
# GPIO.setup(18, GPIO.OUT)
# 
# while True:
#     GPIO.output(16, GPIO.HIGH)
#     time.sleep(3)
#     GPIO.output(16, GPIO.LOW)
#     time.sleep(1)
#     GPIO.output(18, GPIO.HIGH)
#     time.sleep(3)
#     GPIO.output(18, GPIO.LOW)
#     time.sleep(1)

import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

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


def left_Forward(x):
    GPIO.output(left_forward, GPIO.HIGH)
    print("Moving left_forward")
    time.sleep(x)
    GPIO.output(left_forward, GPIO.LOW)

def left_reverse(x):
    GPIO.output(left_backward, GPIO.HIGH)
    print("Moving left_backward")
    time.sleep(x)
    GPIO.output(left_backward, GPIO.LOW)
    
def right_Forward(x):
    GPIO.output(right_forward, GPIO.HIGH)
    print("Moving right_forward")
    time.sleep(x)
    GPIO.output(right_forward, GPIO.LOW)

def right_reverse(x):
    GPIO.output(right_backward, GPIO.HIGH)
    print("Moving right_backward")
    time.sleep(x)
    GPIO.output(right_backward, GPIO.LOW)

for y in range(2):
    
    left_Forward(1)

    #left_reverse(1)

    right_Forward(1)

    #right_reverse(1)
# GPIO.output(left_forward, GPIO.LOW)
# GPIO.output(left_backward, GPIO.LOW)

GPIO.cleanup()
