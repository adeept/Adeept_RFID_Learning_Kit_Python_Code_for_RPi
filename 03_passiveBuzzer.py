#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BZRPin = 12     # Set Pin Phyiscal Pin 12

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(BZRPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(BZRPin, GPIO.LOW)   # Set Buzzer to Off

p = GPIO.PWM(BZRPin, 50) # init frequency: 50HZ
p.start(50)  # Duty cycle: 50%

try:
	while True:
		for f in range(100, 2000, 100):     # Implements a loop increasing frequency
			p.ChangeFrequency(f)
			time.sleep(0.2)
		for f in range(2000, 100, -100):    # Implememnts a loop decreasing frequency
			p.ChangeFrequency(f)
			time.sleep(0.2)
except KeyboardInterrupt:       # When a keyboard interrupt is detected, stop the while loop and cleanup
	p.stop()
	GPIO.cleanup()  # Release GPIO resources
