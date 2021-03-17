import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trigger = 18
echo = 24

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distance():
    GPIO.output(trigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger, GPIO.LOW)
    
    starttime = time.time()
    stoptime = time.time()
    
    while GPIO.input(echo) == 0:
        starttime = time.time()
        
    while GPIO.input(echo) == 1:
        stoptime = time.time()
        
    elapsed = stoptime - starttime
    
    distance = (elapsed * 34300) / 2
    
    return distance
try:
    while True:
        deltad = distance()
        print("Gemessene Entfernung = %.1f cm" % deltad)
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Messung vom User gestoppt")
    GPIO.cleanup()