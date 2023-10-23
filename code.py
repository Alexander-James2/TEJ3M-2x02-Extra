# Created by Alex James
# Created on Oct. 2023
# Template taken from Adafruit site

#This program Blinks the built in LED on the Pi Pico, and then extends the blink by 1 second each loop

int blinkTime = 1000 #this sets variable to 1000ms

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(blinkTime)
    led.value = False
    time.sleep(1)

    blinkTime = blinkTime + 1000