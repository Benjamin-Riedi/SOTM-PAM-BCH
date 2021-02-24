import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarning(False)

stepPin = [placeholder]
dirPin = [placeholder]

GPIO.setup(stepPin, GPIO.OUT)
GPIO.setup(dirPin, GPIO.OUT)

def rightMotorOn(x, stepPin, dirPin):
	if x==1:
		GPIO.output(dirPin, GPIO.LOW)

		GPIO.output(steppin, GPIO.HIGH)
		time.sleep(0.01)
		GPIO.output(steppin, GPIO.HIGH)
		time.sleep(0.01)
	if x==0:
		GPIO.output(dirPin, GPIO.HIGH)

		GPIO.output(stepPin, GPIO.HIGH)
		time.sleep(0.01)
		GPIO.output(stepPin, GPIO.LOW)
		time.sleep(0.01)


