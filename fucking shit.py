import GPIO
import sys
import time

GPIO.setwarnigns(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.output(23, GPIO.HIGH)
time.sleep(3)
GPIUO.output(23, GPIO.LOW)
time.sleep(1)
GPIO.output(24, GPIO.HIGH)
time.sleep(3)
GPIO.output(24, GPIO.LOW)
time.sleep(1)