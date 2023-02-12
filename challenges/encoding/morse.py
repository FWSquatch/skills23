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

CODE = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}

if len(sys.argv) > 1:
    message = sys.argv[1].upper()
else:
    message = "SOS"

for letter in message:
    for symbol in CODE[letter.upper()]:
        if symbol == '-':
            dash()
        elif symbol == '.':
            dot()
        else:
            time.sleep(0.5)
    time.sleep(1)
