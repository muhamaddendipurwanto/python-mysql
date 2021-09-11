#!/usr/bin/env python
"""
 Blinks an LED on digital pin 13
 in 1 second intervals
"""
import Arduino
from Arduino import Arduino
import time



board = Arduino("115200", port="COM10") # plugged in via USB, serial com at rate 115200
board.pinMode(13, "OUTPUT")


while True:
    board.digitalWrite(13, "LOW")
    time.sleep(1)
    board.digitalWrite(13, "HIGH")
    time.sleep(1)
