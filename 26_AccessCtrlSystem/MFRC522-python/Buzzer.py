#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BZRPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BZRPin, GPIO.OUT)
	GPIO.output(BZRPin, GPIO.HIGH)

def beep():
	GPIO.output(BZRPin, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(BZRPin, GPIO.HIGH)
	time.sleep(0.5)

def destroy():
	GPIO.output(BZRPin, GPIO.HIGH)
	GPIO.cleanup()

def test():
	for n in range(0, 10):
		beep()

if __name__ == '__main__':
	setup()
	try:
		test()
	except KeyboardInterrupt:
		destroy()

