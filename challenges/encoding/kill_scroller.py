#!/usr/bin/env python3

import subprocess
from time import time, sleep, localtime
from wiringpi import wiringPiSetupGpio, pinMode, digitalRead, digitalWrite, GPIO
wiringPiSetupGpio()
import sys


CLK = 16
DIO = 17

"""
      A
     ---
  F |   | B
     -G-
  E |   | C
     ---
      D

"""


class TM1637:
    I2C_COMM1 = 0x40
    I2C_COMM2 = 0xC0
    I2C_COMM3 = 0x80
    digit_to_segment = [
        0b0111111, # 0
        0b0000110, # 1
        0b1011011, # 2
        0b1001111, # 3
        0b1100110, # 4
        0b1101101, # 5
        0b1111101, # 6
        0b0000111, # 7
        0b1111111, # 8
        0b1101111, # 9
        0b1110111, # A
        0b1111100, # b
        0b0111001, # C
        0b1011110, # d
        0b1111001, # E
        0b1110001  # F
        ]

    def __init__(self, clk, dio):
        self.clk = clk
        self.dio = dio
        self.brightness = 0x0f

        pinMode(self.clk, GPIO.INPUT)
        pinMode(self.dio, GPIO.INPUT)
        digitalWrite(self.clk, GPIO.LOW)
        digitalWrite(self.dio, GPIO.LOW)

    def bit_delay(self):
        sleep(0.001)
        return
   
    def set_segments(self, segments, pos=0):
        # Write COMM1
        self.start()
        self.write_byte(self.I2C_COMM1)
        self.stop()

        # Write COMM2 + first digit address
        self.start()
        self.write_byte(self.I2C_COMM2 + pos)

        for seg in segments:
            self.write_byte(seg)
        self.stop()

        # Write COMM3 + brightness
        self.start()
        self.write_byte(self.I2C_COMM3 + self.brightness)
        self.stop()

    def start(self):
        pinMode(self.dio, GPIO.OUTPUT)
        self.bit_delay()
   
    def stop(self):
        pinMode(self.dio, GPIO.OUTPUT)
        self.bit_delay()
        pinMode(self.clk, GPIO.INPUT)
        self.bit_delay()
        pinMode(self.dio, GPIO.INPUT)
        self.bit_delay()
  
    def write_byte(self, b):
      # 8 Data Bits
        for i in range(8):

            # CLK low
            pinMode(self.clk, GPIO.OUTPUT)
            self.bit_delay()

            pinMode(self.dio, GPIO.INPUT if b & 1 else GPIO.OUTPUT)

            self.bit_delay()

            pinMode(self.clk, GPIO.INPUT)
            self.bit_delay()
            b >>= 1
      
        pinMode(self.clk, GPIO.OUTPUT)
        self.bit_delay()
        pinMode(self.clk, GPIO.INPUT)
        self.bit_delay()
        pinMode(self.clk, GPIO.OUTPUT)
        self.bit_delay()

        return
def translate(tm,value):
    if value == "0":
        return_val = tm.digit_to_segment[0]
    elif value == "1":
        return_val = tm.digit_to_segment[1]
    elif value == "2":
        return_val = tm.digit_to_segment[2]
    elif value == "3":
        return_val = tm.digit_to_segment[3]
    elif value == "4":
        return_val = tm.digit_to_segment[4]
    elif value == "5":
        return_val = tm.digit_to_segment[5]
    elif value == "6":
        return_val = tm.digit_to_segment[6]
    elif value == "7":
        return_val = tm.digit_to_segment[7]
    elif value == "8":
        return_val = tm.digit_to_segment[8]
    elif value == "9":
        return_val = tm.digit_to_segment[9]
    elif value == "a":
        return_val = tm.digit_to_segment[10]
    elif value == "b":
        return_val = tm.digit_to_segment[11]
    elif value == "c":
        return_val = tm.digit_to_segment[12]
    elif value == "d":
        return_val = tm.digit_to_segment[13]
    elif value == "e":
        return_val = tm.digit_to_segment[14]
    elif value == "f":
        return_val = tm.digit_to_segment[15]
    elif value == "g":
        return_val = tm.digit_to_segment[16]
    else:
        return_val = 0

    return return_val

def scroller(tm,words,delay):
    # Add some pading
    words = "XXXX"+words+"XXXX"
    for x in range(len(words)-3):
        val1 = translate(tm,words[x])
        val2 = translate(tm,words[x+1])
        val3 = translate(tm,words[x+2])
        val4 = translate(tm,words[x+3])
        tm.set_segments([val1,val2,val3,val4])
        sleep(delay)

def convert_to_hex(word):
    h = ' '.join([f'{ord(c):x}' for c in word])
    return h

def show_ip_address(tm):
    ipaddr = subprocess.check_output("hostname -I", shell=True, timeout=1).strip().split(b".")
    for octet in ipaddr:
        tm.set_segments([0, 0, 0, 0])
        sleep(0.1)
        tm.set_segments([tm.digit_to_segment[int(x) & 0xf] for x in octet])
        sleep(0.9)
    #tm.set_segments([0,0,0,0])


def show_clock(tm):
        t = localtime()
        sleep(1 - time() % 1)
        d0 = tm.digit_to_segment[t.tm_hour // 10] if t.tm_hour // 10 else 0
        d1 = tm.digit_to_segment[t.tm_hour % 10]
        d2 = tm.digit_to_segment[t.tm_min // 10]
        d3 = tm.digit_to_segment[t.tm_min % 10]
        tm.set_segments([d0, 0x80 + d1, d2, d3])
        sleep(.5)
        tm.set_segments([d0, d1, d2, d3])

# Rolling animation (used to separate messages)
def roll():
    for x in range (2):
        tm.set_segments([0b1000000,0b1000000,0b1000000,0b1000000])
        sleep(.01)
        tm.set_segments([0b0000100,0b0000100,0b0000100,0b0000100])
        sleep(.01)
        tm.set_segments([0b0001000,0b0001000,0b0001000,0b0001000])
        sleep(.01)
        tm.set_segments([0b0010000,0b0010000,0b0010000,0b0010000])
        sleep(.01)

def blank():
        tm.set_segments([0b0000000,0b0000000,0b0000000,0b0000000])

if __name__ == "__main__":
    tm = TM1637(CLK, DIO)

blank()
