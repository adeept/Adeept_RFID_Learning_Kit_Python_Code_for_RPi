#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 06_relay.py
# Description : Toggle a relay.
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import RPi.GPIO as GPIO
import time

RelayPin = 12    # pin12

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)         # Numbers pins by physical location
	GPIO.setup(RelayPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(RelayPin, GPIO.HIGH)

def loop():
	while True:
		print '...clsoe'
		GPIO.output(RelayPin, GPIO.LOW)
		time.sleep(0.5)
		print 'open...'
		GPIO.output(RelayPin, GPIO.HIGH)
		time.sleep(0.5)

def destroy():
	GPIO.output(RelayPin, GPIO.HIGH)
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

