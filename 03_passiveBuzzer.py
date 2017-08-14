#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 03_passiveBuzzer.py
# Description : make a passive buzzer beep.
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import RPi.GPIO as GPIO
import time

BZRPin = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(BZRPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(BZRPin, GPIO.LOW)

p = GPIO.PWM(BZRPin, 50) # init frequency: 50HZ
p.start(50)  # Duty cycle: 50%

try:
	while True:
		for f in range(100, 2000, 100):
			p.ChangeFrequency(f)
			time.sleep(0.2)
		for f in range(2000, 100, -100):
			p.ChangeFrequency(f)
			time.sleep(0.2)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()


