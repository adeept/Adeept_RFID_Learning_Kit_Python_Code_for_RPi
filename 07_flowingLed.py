#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 07_flowingLed.py
# Description : flowing LED
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import RPi.GPIO as GPIO
import time

pins = [11, 12, 13, 15, 16, 18, 22, 7]

def setup():
	GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)   # Set all pins' mode is output
		GPIO.output(pin, GPIO.LOW) # Set all pins to high(+3.3V) to off led

def loop():
	while True:
		for pin in pins:
			GPIO.output(pin, GPIO.HIGH)
			time.sleep(0.2)
			GPIO.output(pin, GPIO.LOW)

def destroy():
	for pin in pins:
		GPIO.output(pin, GPIO.LOW)    # turn off all leds
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

