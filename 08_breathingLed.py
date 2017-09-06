#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 12                   #GPIO pin declaration. same as diagram

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(LedPin, GPIO.LOW)  # Set pin to low(0V)

p = GPIO.PWM(LedPin, 1000)     # set Frequece to 1KHz
p.start(0)                     # Start PWM output, Duty Cycle = 0

try:
	while True:
		for dc in range(0, 85, 5):   # Increase duty cycle: 0~100
			p.ChangeDutyCycle(dc)     # Change duty cycle
			time.sleep(0.05)
		time.sleep(1)
		for dc in range(85, -1, -5): # Decrease duty cycle: 100~0
			p.ChangeDutyCycle(dc)
			time.sleep(0.05)
		time.sleep(1)
except KeyboardInterrupt:
	p.stop()
	GPIO.output(LedPin, GPIO.HIGH)    # turn off all leds
	GPIO.cleanup()
