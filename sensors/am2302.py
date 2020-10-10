import sys
import math

import Adafruit_DHT

sensor = Adafruit_DHT.AM2302

def getTemperature(pin):
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	return math.floor(temperature*100)/100

def getHumidity(pin):
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	return math.floor(humidity*100)/100
