import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.IN)

while True:
	time.sleep(1)
	h=GPIO.input(17)
	print(h)





