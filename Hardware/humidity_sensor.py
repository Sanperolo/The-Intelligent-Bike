# Humidity Sensor
import Adafruit_DHT as dht    # Importing Adafruit library for DHT22
from time import sleep           # Impoting sleep from time library to add delay
from lcd_display_16x2 import lcd_init, lcd_string, LCD_LINE_1, LCD_LINE_2

lcd_init()
	
def main():
	# lcd_init()
	
	while 1:                # Loop will run forever
		humi, temp = dht.read_retry(dht.DHT22, 23)  # Reading humidity and temperature
		print('Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(temp, humi))
		# lcd_string("Temp: {0:0.1f}*C".format(temp),LCD_LINE_1)
		# lcd_string("Humidity: {0:0.1f}%".format(humi),LCD_LINE_2)
		sleep(3)


if __name__ == '__main__':
	main()
