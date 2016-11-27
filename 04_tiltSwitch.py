#!/usr/bin/env python
import RPi.GPIO as GPIO

TiltPin = 12    # Set Physical Pin number
LedPin  = 11    # Set Phyiscal Pin number

Led_status = 1

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
	GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led

def swLed(ev=None):
	global Led_status
	Led_status = not Led_status
	GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
	if Led_status == 1:
		print 'led off...'
	else:
		print '...led on'

def loop():
	GPIO.add_event_detect(TiltPin, GPIO.FALLING, callback=swLed) # wait for falling
	while True:
		pass   # Don't do anything

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

