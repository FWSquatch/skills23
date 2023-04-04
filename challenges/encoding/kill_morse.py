#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import sys

message = "ATOWN2023"
ledPin=27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT,initial=GPIO.LOW)

def dot():
	GPIO.output(ledPin,1)
	time.sleep(0.2)
	GPIO.output(ledPin,0)
	time.sleep(0.2)

def dash():
	GPIO.output(ledPin,1)
	time.sleep(0.5)
	GPIO.output(ledPin,0)
	time.sleep(0.2)

def blank():
	GPIO.output(ledPin,0)

blank()
