#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gpiozero import LED
from time import sleep

led = LED(25)

delay = 1
iterations = 50
for i in range(0, iterations-1):
    led.on()
    print('LED On #%i' % i)
    sleep(delay)
    led.off()
    print('LED Off #%i' % i)
    sleep(delay)
    