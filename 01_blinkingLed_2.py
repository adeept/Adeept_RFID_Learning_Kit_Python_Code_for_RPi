#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11 this declares a pin to use

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led

def loop():
	while True:
		print '...led on'
		GPIO.output(LedPin, GPIO.LOW)  # led on
		time.sleep(0.5)
		print 'led off...'
		GPIO.output(LedPin, GPIO.HIGH) # led off
		time.sleep(0.5)

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
