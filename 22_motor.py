#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

STATUS_LED         = 10

BTN_RUN_STOP       = 11
BTN_DIRECTION      = 12
BTN_SPEED_INCREASE = 13
BTN_SPEED_DECREASE = 15

MotorPin_A         = 16
MotorPin_B         = 18

g_sta =  1
g_dir =  1
speed = 50

pwm_B = 0

def motorStop():
	GPIO.output(MotorPin_A, GPIO.HIGH)
	GPIO.output(MotorPin_B, GPIO.LOW)

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(STATUS_LED, GPIO.OUT)   # pin mode --- output
	GPIO.setup(BTN_RUN_STOP, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set pin mode as input, and pull it to high level.
	GPIO.setup(BTN_DIRECTION, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(BTN_SPEED_INCREASE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(BTN_SPEED_DECREASE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(MotorPin_A, GPIO.OUT)
	GPIO.setup(MotorPin_B, GPIO.OUT)
	motorStop()
	global pwm_B
	pwm_B = GPIO.PWM(MotorPin_B, 2000) # create pwm and set frequece to 2KHz

def motor(status, direction, speed):
	global pwm_B
	if status == 1:  # run
		GPIO.output(STATUS_LED, GPIO.LOW) # led on
		if direction == 1:
			GPIO.output(MotorPin_A, GPIO.HIGH)
			pwm_B.start(100)
			pwm_B.ChangeDutyCycle(100-speed)
		else:
			GPIO.output(MotorPin_A, GPIO.LOW)
			pwm_B.start(0)
			pwm_B.ChangeDutyCycle(speed)
	else:  # stop
		GPIO.output(STATUS_LED, GPIO.HIGH) # led off
		motorStop()

def btnScan():
	global g_sta
	global g_dir
	global speed
	if GPIO.input(BTN_RUN_STOP) == GPIO.LOW:
		time.sleep(0.01)
		if GPIO.input(BTN_RUN_STOP) == GPIO.LOW:
			g_sta = not g_sta
			print 'g_sta = %d', g_sta
		while not GPIO.input(BTN_RUN_STOP):
			pass
	if GPIO.input(BTN_DIRECTION) == GPIO.LOW:
		time.sleep(0.01)
		if GPIO.input(BTN_DIRECTION) == GPIO.LOW:
			g_dir = not g_dir
			print 'g_dir = %d', g_dir
		while not GPIO.input(BTN_DIRECTION):
			pass
	if GPIO.input(BTN_SPEED_INCREASE) == GPIO.LOW:
		time.sleep(0.01)
		if GPIO.input(BTN_SPEED_INCREASE) == GPIO.LOW:
			speed += 1
			if speed > 100:
				speed = 100
			print 'speed = %d', speed
		while not GPIO.input(BTN_SPEED_INCREASE):
			pass
	if GPIO.input(BTN_SPEED_DECREASE) == GPIO.LOW:
		time.sleep(0.01)
		if GPIO.input(BTN_SPEED_DECREASE) == GPIO.LOW:
			speed -= 1
			if speed < 0:
				speed = 0
			print 'speed = %d', speed
		while not GPIO.input(BTN_SPEED_DECREASE):
			pass

def loop():
	while True:
#		print 'test....2...'
		btnScan()
#		print 'test....3...'
		global g_sta
		global g_dir 
		global speed
		motor(g_sta, g_dir, speed)

def destroy():
	motorStop()
	GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()

