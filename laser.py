import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.IN)

while True:
	time.sleep(1)
	h=GPIO.input(23)
	print(h)





