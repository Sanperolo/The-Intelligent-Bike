#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Shared imports
import time

# Sensors imports
import RPi.GPIO as GPIO
import Adafruit_DHT as dht    # Importing Adafruit library for DHT22
from lcd_display_16x2 import lcd_init, lcd_string, lcd_byte, LCD_LINE_1, LCD_LINE_2
from rain_sensor import setup as rain_sensor_setup 
from rain_sensor import output as rain_sensor_output

# MQTT imports
import paho.mqtt.client as mqtt

# Unify all the sensors in order to send all the sensor data to the Backend with MQTT Protocol 
# ----------------------------------------------------
# 1. Raindrop Sensor 
# 		PIN: G20
# 2. Humidity Sensor
# 		PIN: G13
# 3. Led Rainning Advise
# 		PIN: G04

PIN_RAIN_SENSOR = 20
PIN_HUMIDITY_SENSOR = 13
PIN_LED = 4

# -- MQTT --
# Configuration
#	HOST
# 	PORT
# 	URL_TOPIC

# -- Online MQTT Brokers for Testing --
# Mosquitto	 	 iot.eclipse.org			1883 / 8883	n/a
# HiveMQ	 	 broker.hivemq.com			1883	8000
# Mosquitto	 	 test.mosquitto.org			1883 / 8883 / 8884	8080 / 8081
# mosca	 	 	 test.mosca.io				1883	80
# HiveMQ	 	 broker.mqttdashboard.com	1883

HOST = "iot.eclipse.org"		# Default
URL_TOPIC = "sensor/data/"       # send messages to this topic
PORT = 1883

# Mqtt Global Setup 
client = mqtt.Client()
client.connect(HOST, PORT, 60)
client.loop_start()

def setup():
	GPIO.setwarnings(False)
	rain_sensor_setup(PIN_RAIN_SENSOR)
	lcd_init()
	GPIO.setmode(GPIO.BCM) # function to set up the LEDs
	GPIO.setup(PIN_LED, GPIO.OUT, initial=GPIO.LOW) #HIGH=1 LOW=0 

def publish_data_mqtt(isRaining, humidity, temperature):
	client.publish(URL_TOPIC + "rain", isRaining)
	client.publish(URL_TOPIC + "humidity", humidity)
	client.publish(URL_TOPIC + 	"temperature", temperature)

def led_rain_led(tmp):
	GPIO.output(PIN_LED, GPIO.HIGH) if tmp == 0 else GPIO.output(PIN_LED, GPIO.LOW)
		 # turn on led									turn off led

def isRaining(tmp):
	return True if tmp == 0 else False

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
		
		# Publish Data in MQTT
		publish_data_mqtt(isRaining(tmp), humi, temp)
		
		time.sleep(1)
	
if __name__ == '__main__':
	setup()
	main()
