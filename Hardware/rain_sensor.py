#!/usr/bin/python
# RainDrop Sensor 

#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math

PIN_SENSOR = 19
GPIO.setmode(GPIO.BCM)

def setup(DO):
	GPIO.setup(DO, GPIO.IN)

def output(x):
	if x == 1:
		print('')
		print('   ***************')
		print('   * Not raining *')
		print('   ***************')
		print('')
	if x == 0:
		print('')
		print('   *************')
		print('   * Raining!! *')
		print('   *************')
		print('')

def loop():
	status = 1
	while True:
		tmp = GPIO.input(PIN_SENSOR);
		output(tmp)
		time.sleep(1)

if __name__ == '__main__':
	try:
		setup(PIN_SENSOR)
		loop()
	except KeyboardInterrupt: 
		pass	
