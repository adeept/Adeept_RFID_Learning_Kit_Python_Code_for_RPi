#!/usr/bin/env python
from socket import *
from time import ctime
import RPi.GPIO as GPIO

LedPin = 11

HOST = ''
PORT = 8080
BUFSIZ = 1024       # Size of the buffer
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)    # Create a socket
tcpSerSock.bind(ADDR)    # Bind the IP address and port number
tcpSerSock.listen(5) 

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led

def loop():
	while True:
		print 'Waiting for connection...'
		tcpCliSock, addr = tcpSerSock.accept()
		print '...connected from :', addr     # Print the IP address of the client connected with the server
		while True:
			data = tcpCliSock.recv(BUFSIZ)    # Receive data sent from the client
			if not data:
				break
			if data == 'ON':
				GPIO.output(LedPin, GPIO.LOW)
				print 'led on'
			elif data == 'OFF':
				GPIO.output(LedPin, GPIO.HIGH)
				print 'led off'
			else:
				print 'error cmd !'
		tcpSerSock.close()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		tcpSerSock.close()

