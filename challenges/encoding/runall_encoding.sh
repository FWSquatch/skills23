#!/bin/bash

BASE_DIR="/opt/encoding"
HEX_MSG="skills{Easy_peasy}"
MORSE_MSG="skillsDotdotdash"
BIN_MSG="skills{Take_a_byte}"
NEO_MSG="skills{Rainbow_blinkies}"

sudo $BASE_DIR/scroller.py $HEX_MSG .2 &
sudo $BASE_DIR/morse.py $MORSE_MSG 1 &
sudo $BASE_DIR/byte.py $BIN_MSG 1 &
sudo $BASE_DIR/pix.py $NEO_MSG 1 &



