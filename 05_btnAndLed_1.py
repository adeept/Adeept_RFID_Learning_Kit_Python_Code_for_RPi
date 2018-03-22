#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 05_btnAndLed_1.py
# Description : toggle an LED by button.
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import RPi.GPIO as GPIO
import time

LedPin = 37    # pin37 --- led
BtnPin = 40    # pin40 --- button

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.output(LedPin, GPIO.LOW) # Set LedPin LOW(+3.3V) to make led off

def loop():
	while True:
		if GPIO.input(BtnPin) == GPIO.HIGH: # Check whether the button is pressed or not.
			print '...led on'
			GPIO.output(LedPin, GPIO.HIGH)  # led on
			time.sleep(0.3)
		else:
			print 'led off...'
			GPIO.output(LedPin, GPIO.LOW) # led off
			time.sleep(0.3)
def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

