#!/usr/bin/env python
import RPi.GPIO as GPIO
import ADC0832
import time

leds = [11,12,13,15,16,18,22,7,3,5]

def ADC0832Init():
	ADC0832.setup()

def ledBarInit():
	GPIO.setmode(GPIO.BOARD)
	for pin in leds:
		GPIO.setup(pin, GPIO.OUT)

def ledBarCtrl(n):
	if n > 10 or n < 0:
		print 'Wrong argument, n = [0~10]'
		return
	for i in range(0, n):
		GPIO.output(leds[i], GPIO.LOW)
	for i in range(0, 10-n):
		GPIO.output(leds[n+i], GPIO.HIGH)

def ledBarDestory():
	for pin in leds:
		GPIO.output(pin, GPIO.HIGH)
	GPIO.cleanup()

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min 

def loop():
	while True:
		res = ADC0832.getResult()
		print 'res = %d' % res
		num = map(res, 0, 255, 0, 10)
		ledBarCtrl(num)
		time.sleep(0.2)

if __name__ == '__main__':
	ADC0832Init()
	ledBarInit()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		ledBarDestory()
		print 'The end !'
