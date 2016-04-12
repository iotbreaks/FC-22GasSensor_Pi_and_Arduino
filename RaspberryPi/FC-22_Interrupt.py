#!/usr/bin/env python2.7
#########################################################
## FC-22_Interrupt.py
## Created by Kenny from www.iotbreaks.vn, April 12, 2016.
## Released into the public domain.
## Tutorial: 
#########################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledOutPin=17
gasInPin=18
readValue=1 # default is 1 as Gas sensor deactivated

GPIO.setup(ledOutPin, GPIO.OUT)
GPIO.setup(gasInPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  

def gasSensorDidChange(pin): 
	print("Detect changed of Gas sensor to " + str(GPIO.input(gasInPin)))
	readValue = GPIO.input(gasInPin)
	GPIO.output(ledOutPin, readValue)

GPIO.add_event_detect(gasInPin, GPIO.BOTH, callback=gasSensorDidChange)
	
try:
	GPIO.output(ledOutPin, readValue)
	print("Detecting....")
	raw_input("Press anykey to finish>")  

except KeyboardInterrupt:  
    GPIO.cleanup() # clean up GPIO on CTRL+C exit 

GPIO.cleanup()
