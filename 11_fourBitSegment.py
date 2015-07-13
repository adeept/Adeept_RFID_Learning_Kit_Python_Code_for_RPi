#!/usr/bin/env python  

import RPi.GPIO as GPIO  
import time  

BIT0 = 3   
BIT1 = 5  
BIT2 = 24  
BIT3 = 26  

segCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]  #0~9  
pins = [11,12,13,15,16,18,22,7,3,5,24,26]  
bits = [BIT0, BIT1, BIT2, BIT3]  

def print_msg():  
	print 'Program is running...'  
	print 'Please press Ctrl+C to end the program...'  

def digitalWriteByte(val):  
	GPIO.output(11, val & (0x01 << 0))  
	GPIO.output(12, val & (0x01 << 1))  
	GPIO.output(13, val & (0x01 << 2))  
	GPIO.output(15, val & (0x01 << 3))  
	GPIO.output(16, val & (0x01 << 4))  
	GPIO.output(18, val & (0x01 << 5))  
	GPIO.output(22, val & (0x01 << 6))  
	GPIO.output(7,  val & (0x01 << 7))  

def display_1():  
	GPIO.output(BIT0, GPIO.LOW)   
	for i in range(10):  
		digitalWriteByte(segCode[i])  
		time.sleep(0.5)  

def display_2():  
	for bit in bits:  
		GPIO.output(bit, GPIO.LOW)   
	for i in range(10):  
		digitalWriteByte(segCode[i])  
		time.sleep(0.5)  

def display_3(num):  
	b0 = num % 10  
	b1 = num % 100 / 10   
	b2 = num % 1000 / 100  
	b3 = num / 1000  
	if num < 10:  
		GPIO.output(BIT0, GPIO.LOW)   
		GPIO.output(BIT1, GPIO.HIGH)   
		GPIO.output(BIT2, GPIO.HIGH)   
		GPIO.output(BIT3, GPIO.HIGH)   
	 	digitalWriteByte(segCode[b0])  
	elif num >= 10 and num < 100:  
		GPIO.output(BIT0, GPIO.LOW)  
		digitalWriteByte(segCode[b0])  
		time.sleep(0.002)  
		GPIO.output(BIT0, GPIO.HIGH)   
		GPIO.output(BIT1, GPIO.LOW)  
		digitalWriteByte(segCode[b1])  
		time.sleep(0.002)  
	 	GPIO.output(BIT1, GPIO.HIGH)  
	elif num >= 100 and num < 1000:  
		GPIO.output(BIT0, GPIO.LOW)  
		digitalWriteByte(segCode[b0])  
		time.sleep(0.002)  
		GPIO.output(BIT0, GPIO.HIGH)   
		GPIO.output(BIT1, GPIO.LOW)  
		digitalWriteByte(segCode[b1])  
		time.sleep(0.002)  
		GPIO.output(BIT1, GPIO.HIGH)  
		GPIO.output(BIT2, GPIO.LOW)  
		digitalWriteByte(segCode[b2])  
		time.sleep(0.002)  
	 	GPIO.output(BIT2, GPIO.HIGH)   
	elif num >= 1000 and num < 10000:  
		GPIO.output(BIT0, GPIO.LOW)  
		digitalWriteByte(segCode[b0])  
		time.sleep(0.002)  
		GPIO.output(BIT0, GPIO.HIGH)   
		GPIO.output(BIT1, GPIO.LOW)  
		digitalWriteByte(segCode[b1])  
		time.sleep(0.002)  
		GPIO.output(BIT1, GPIO.HIGH)  
		GPIO.output(BIT2, GPIO.LOW)  
		digitalWriteByte(segCode[b2])  
		time.sleep(0.002)  
		GPIO.output(BIT2, GPIO.HIGH)   
		GPIO.output(BIT3, GPIO.LOW)  
		digitalWriteByte(segCode[b3])  
		time.sleep(0.002)  
	 	GPIO.output(BIT3, GPIO.HIGH)   
	else:  
		 print 'Out of range, num should be 0~9999 !'  

def setup():  
	GPIO.setmode(GPIO.BOARD)    #Number GPIOs by its physical location  
	for pin in pins:  
		GPIO.setup(pin, GPIO.OUT)    #set all pins' mode is output  
		GPIO.output(pin, GPIO.HIGH)  #set all pins are high level(3.3V)  

def loop():  
	while True:  
		print_msg()  
		display_1()  
		time.sleep(1)  
		display_2()  
		time.sleep(1)  

		tmp = int(raw_input('Please input a num(0~9999):'))  
		for i in range(500):  
			display_3(tmp)  
		time.sleep(1)  

def destroy():   #When program ending, the function is executed.   
	for pin in pins:    
		GPIO.output(pin, GPIO.LOW) #set all pins are low level(0V)   
		GPIO.setup(pin, GPIO.IN)   #set all pins' mode is input  

if __name__ == '__main__': #Program starting from here   
	setup()   
	try:  
		loop()    
	except KeyboardInterrupt:    
		destroy()    
