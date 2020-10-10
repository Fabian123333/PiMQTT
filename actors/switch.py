import RPi.GPIO as GPIO

def __init__(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

def getStatus(pin):
	return GPIO.input(pin)

def setOn(pin):
	GPIO.output(pin, GPIO.HIGH)

def setOff(pin):
	GPIO.output(pin, GPIO.LOW)

def toggle(pin):
	if(getStatus(pin) == 1):
		setOff(pin)
	else:
		setOn(pin)