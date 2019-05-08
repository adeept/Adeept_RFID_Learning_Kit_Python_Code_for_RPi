#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 08_breathingLed.py
# Description : breathing LED.
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import RPi.GPIO as GPIO
import time

LedPin = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(LedPin, GPIO.LOW)  # Set pin to low(0V)

p = GPIO.PWM(LedPin, 1000)     # set Frequece to 1KHz
p.start(0)                     # Start PWM output, Duty Cycle = 0
#for led in LedPin:
# 	p = GPIO.PWM(led, 1000)     # set Frequece to 1KHz
#	p.start(0)                     # Start PWM output, Duty Cycle = 0
try:
	while True:
		for dc in range(0, 101, 4):   # Increase duty cycle: 0~100
			p.ChangeDutyCycle(dc)     # Change duty cycle
			time.sleep(0.05)
			time.sleep(1)
		for dc in range(100, -1, -4): # Decrease duty cycle: 100~0
			p.ChangeDutyCycle(dc)
			time.sleep(0.05)
			time.sleep(1)
except KeyboardInterrupt:
	p.stop()
	GPIO.output(LedPin, GPIO.LOW)    # turn off all leds
	GPIO.cleanup()

