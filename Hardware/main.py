#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import Adafruit_DHT as dht    # Importing Adafruit library for DHT22
from lcd_display_16x2 import lcd_init, lcd_string, lcd_byte, LCD_LINE_1, LCD_LINE_2
from rain_sensor import setup as rain_sensor_setup 
from rain_sensor import output as rain_sensor_output
import time

# Unify all the sensors in order to send all the sensor data to the Backend with MQTT Protocol 
# ----------------------------------------------------
# 1. Raindrop Sensor 
# 		PIN: G19
# 2. Humidity Sensor
# 		PIN: G13
# 3. Led Rainning Advise
# 		PIN: G04

PIN_RAIN_SENSOR = 20
PIN_HUMIDITY_SENSOR = 13
PIN_LED = 4

def setup():
	GPIO.setwarnings(False)
	rain_sensor_setup(PIN_RAIN_SENSOR)
	lcd_init()
	GPIO.setmode(GPIO.BCM) # function to set up the LEDs
	GPIO.setup(PIN_LED, GPIO.OUT, initial=GPIO.LOW) #HIGH=1 LOW=0 

def led_rain_led(tmp):
	GPIO.output(PIN_LED, GPIO.HIGH) if tmp == 0 else GPIO.output(PIN_LED, GPIO.LOW)
		 # turn on led									turn off led

def main():
	while True:
		# Rain Sensor
		tmp = GPIO.input(PIN_RAIN_SENSOR);
		rain_sensor_output(tmp)
		
		# Humidity Sensor in Display
		humi, temp = dht.read_retry(dht.DHT22, PIN_HUMIDITY_SENSOR)  # Reading humidity and temperature
		
		lcd_string("Temp: {0:0.1f}*C".format(temp),LCD_LINE_1)
		lcd_string("Humidity: {0:0.1f}%".format(humi),LCD_LINE_2)
		
		# Led Rain Warning 
		led_rain_led(tmp)
		
		time.sleep(1)
	
if __name__ == '__main__':
	setup()
	main()
