#!/bin/bash

BASE_DIR="/opt/encoding"

pkill python3
$BASE_DIR/kill_pix.py

pkill byte.py
$BASE_DIR/kill_byte.py

pkill scroller.py
$BASE_DIR/kill_scroller.py

pkill morse.py
$BASE_DIR/kill_morse.py
