#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Uses a potentiometer to manually adjust resistance to LED, creating a dimmer.

Parts needed:
    Raspberry Pi
    Breadboard
    10k ohm potentiometer
    MCP3008 chip
    5mm LED
    330 ohm resistor
    Jumper wires
"""

from gpiozero import PWMLED, MCP3008
from time import sleep

pot = MCP3008(0)
led = PWMLED(17)

while True:
    if(pot.value < 0.001):
        led.value = 0
    else:
        led.value = pot.value
        print(pot.value)
        sleep(0.1)
        