import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# HOST = "192.168.110.1"
# HOST = "127.0.0.1"
HOST = "iot.eclipse.org"

led = 16

GPIO.setmode(GPIO.BCM) # function to set up the LEDs

GPIO.setup(led, GPIO.OUT, initial = GPIO.LOW) #HIGH=1 LOW=0 

pub_topic = "sensor/data"       # send messages to this topic

############### MQTT section ##################
client = mqtt.Client()
client.connect(HOST, 1883, 60)
client.loop_start()

cont = 1
while True:
	client.publish(pub_topic, "Hello World " + str(cont))
	cont = cont + 1
	print("Send!")
	time.sleep(1)
	GPIO.output(led, GPIO.HIGH) # turn on led
	time.sleep(5)
	GPIO.output(led, GPIO.LOW) # turn off led
