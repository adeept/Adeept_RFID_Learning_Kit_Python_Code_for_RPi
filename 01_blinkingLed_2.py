#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 01_blinkingLed_2.py
# Description : make an led blinking.
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import RPi.GPIO as GPIO
import time

LedPin = 37    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(LedPin, GPIO.LOW) # Set pin to high(+3.3V) to ON the led

def loop():
	while True:
		print '...led on'
		GPIO.output(LedPin, GPIO.HIGH)  # led OFF
		time.sleep(0.5)
		print 'led off...'
		GPIO.output(LedPin, GPIO.LOW) # led ON
		time.sleep(0.5)

def destroy():
	GPIO.output(LedPin, GPIO.LOW)     # led ON
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

