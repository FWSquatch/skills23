#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import sys

# Define your pinout
pins = [12,20,21,5,6,13,19,26]

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin,GPIO.OUT,initial=GPIO.LOW)

# Turn off ALL pins
def blank():
    for pin in pins:
        GPIO.output(pin,0)
blank()
