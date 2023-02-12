#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import sys

# Define your pinout
pins = [12,20,21,5,6,13,19,26]

# Grab arguments
message = sys.argv[1]
if len(sys.argv) > 1:
    delay = float(sys.argv[2])
else:
    delay = 1

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin,GPIO.OUT,initial=GPIO.LOW)

# Wipe animation between runs
def wipe():
    for pin in pins:
        GPIO.output(pin,1)
        time.sleep(0.05)
        GPIO.output(pin,0)
        time.sleep(0.05)
    for pin in list(reversed(pins)):
        GPIO.output(pin,1)
        time.sleep(0.05)
        GPIO.output(pin,0)
        time.sleep(0.05)
    time.sleep(delay)

# Turn off ALL pins
def blank():
    for pin in pins:
        GPIO.output(pin,0)

# Display byte on led array
def show_byte(byte):
    index = 0
    for pin in pins:
        GPIO.output(pin, int(byte[index]))
        index += 1
        
# Convert from ASCII to binary
def convert_to_bin(data):
    binary = ' '.join(format(ord(i),'b').zfill(8) for i in data)
    return binary.split()

def display_string(msg_string):
    for byte in (convert_to_bin(msg_string)):
        show_byte(byte)
        time.sleep(delay)
        blank()
        time.sleep(delay)

for i in range(3):
    wipe()
    display_string(message)
