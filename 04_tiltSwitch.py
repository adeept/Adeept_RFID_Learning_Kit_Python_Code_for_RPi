#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 04_tiltSwitch.py
# Description : Control an LED by tilit switch.
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import RPi.GPIO as GPIO

LedPin  = 11
TiltPin = 12

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
	GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led

def loop():
	while True:
		if GPIO.input(TiltPin) == GPIO.LOW:
			GPIO.output(LedPin, GPIO.LOW)
			print 'LED ON...'
		else:
			GPIO.output(LedPin, GPIO.HIGH)
			print '...LED OFF'

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

