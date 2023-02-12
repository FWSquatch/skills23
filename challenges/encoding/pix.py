#!/usr/bin/env python3
import time
import board
import neopixel
import sys

# NeoPixels data pin
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 2

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

# Grab arguments
message = sys.argv[1]
print('length',len(sys.argv))
if len(sys.argv) > 2:
    delay = float(sys.argv[2])
else:
    delay = 1

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)
cyan = (0,255,255)
purple = (255,0,255)

code = {
    "A": [red,red],
    "B" : [red,green],
    "C" : [red,blue],
    "D" : [red,yellow],
    "E" : [red,white],
    "F" : [red,cyan],
    "G" : [red,purple],
    "H" : [green,red],
    "I" : [green,green],
    "J" : [green,blue],
    "K" : [green,yellow],
    "L" : [green,white],
    "M" : [green,cyan],
    "N" : [green,purple],
    "O" : [blue,red],
    "P" : [blue,green],
    "Q" : [blue,blue],
    "R" : [blue,yellow],
    "S" : [blue,white],
    "T" : [blue,cyan],
    "U" : [blue,purple],
    "V" : [yellow,red],
    "W" : [yellow,green],
    "X" : [yellow,blue],
    "Y" : [yellow,yellow],
    "Z" : [yellow,white],
    "ONE" : [yellow,cyan],
    "TWO" : [yellow,purple],
    "THREE" : [white,red],
    "FOUR" : [white,green],
    "FIVE" : [white,blue],
    "SIX" : [white,yellow],
    "SEVEN" : [white,white],
    "EIGHT" : [white,cyan],
    "NINE" : [white,purple],
    "ZERO" : [cyan,red],
    "DOT" : [cyan,green],
    "BANG" : [cyan,blue],
    "QUESTION" : [cyan,yellow],
    "COMMA" : [cyan,white],
    "OPAREN" : [cyan,cyan],
    "CPAREN" : [cyan,purple],
    "UNDER" : [purple,red],
    "OCURLY" : [purple,green],
    "CCURLY" : [purple,blue],
    "AT" : [purple,yellow],
    "HASH" : [purple,white],
    "CASH" : [purple,cyan],
    "DASH" : [purple,purple]
}

def pix_off():
    pixels.fill((0,0,0))
    pixels.show()

def convert(word):
    for char in word:
        if any(map(str.isupper,char)):
            display(char)
        else:
            display(spec_chars(char))
        
def spec_chars(char):
    if char == '1':
        return 'ONE'
    elif char == '2':
        return 'TWO'
    elif char == '3':
        return 'THREE'
    elif char == '4':
        return 'FOUR'
    elif char == '5':
        return 'FIVE'
    elif char == '6':
        return 'SIX'
    elif char == '7':
        return 'SEVEN'
    elif char == '8':
        return 'EIGHT'
    elif char == '9':
        return 'NINE'
    elif char == '0':
        return 'ZERO'
    elif char == '.':
        return 'DOT'
    elif char == '!':
        return 'BANG'
    elif char == '?':
        return 'QUESTION'
    elif char == ',':
        return 'COMMA'
    elif char == '(':
        return 'OPAREN'
    elif char == ')':
        return 'CPAREN'
    elif char == '_':
        return 'UNDER'
    elif char == '{':
        return 'OCURLY'
    elif char == '}':
        return 'CCURLY'
    elif char == '@':
        return 'AT'
    elif char == '#':
        return 'HASH'
    elif char == '$':
        return 'CASH'
    elif char == '-':
        return 'DASH'

def display(char):
    pixels[0] = code[char][0]
    pixels[1] = code[char][1]
    pixels.show()
    time.sleep(delay)
    pix_off()
    time.sleep(.1)

convert(message)

pix_off()

#    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
#
