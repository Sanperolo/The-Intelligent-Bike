import RPi.GPIO as GPIO
import time
import thread

redled = 17 #Red LED connected to G17
redbtn = 16 # red button connected G16

GPIO.setmode(GPIO.BCM) # function to set up the LEDs

GPIO.setup(redled, GPIO.OUT, initial = GPIO.LOW) #HIGH=1 LOW=0 
GPIO.setup(redbtn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #HIGH=1 LOW=0 
	
def blinked():
	for i in range (1, 100):
		GPIO.output(redled, GPIO.HIGH) # turn on led
		time.sleep(0.10)
		GPIO.output(redled, GPIO.LOW) # turn off led
		time.sleep(0.10)
		
def btnPressed(channel):
	thread.start_new_thread(blinked,())
	
	
GPIO.add_event_detect(redbtn, GPIO.RISING, callback = btnPressed, bouncetime = 300)

while True:
	time.sleep(10)
	pass

