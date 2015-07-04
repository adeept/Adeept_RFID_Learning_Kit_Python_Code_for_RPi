#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 01_blinkingLed_1.py
# Description : make an led blinking.
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led

try:
	while True:
		print '...led on'
		GPIO.output(LedPin, GPIO.LOW)  # led on
		time.sleep(0.5)
		print 'led off...'
		GPIO.output(LedPin, GPIO.HIGH) # led off
		time.sleep(0.5)
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

