#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 17_photoResistor.py
# Description : ...
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import ADC0832
import time

def init():
	ADC0832.setup()

def loop():
	while True:
		res = ADC0832.getResult() - 80
		if res < 0:
			res = 0
		if res > 100:
			res = 100
		print 'res = %d' % res
		time.sleep(0.2)

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'

