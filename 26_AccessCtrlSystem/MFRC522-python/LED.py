#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LEDPin = 12

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LEDPin, GPIO.OUT)
	GPIO.output(LEDPin, GPIO.HIGH)

def led():
	GPIO.output(LEDPin, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(LEDPin, GPIO.HIGH)
	time.sleep(0.5)

def destroy():
	GPIO.output(LEDPinPin, GPIO.HIGH)
	GPIO.cleanup()

def test():
	for n in range(0, 10):
		led()

if __name__ == '__main__':
	setup()
	try:
		test()
	except KeyboardInterrupt:
		destroy()

