#!/usr/bin/env python2.7
#########################################################
## FC-22_Polling.py
## Created by Kenny from www.iotbreaks.vn, April 12, 2016.
## Released into the public domain.
## Tutorial: 
#########################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledOutPin=17
gasInPin=18

GPIO.setup(ledOutPin, GPIO.OUT)
GPIO.setup(gasInPin, GPIO.IN)

while 1 : 
	readValue = GPIO.input(gasInPin)
	GPIO.output(ledOutPin, readValue) 
	time.sleep(0.2)

GPIO.cleanup()
