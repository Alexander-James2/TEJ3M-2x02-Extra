# Created by Alex James
# Created on Oct. 2023

#This program Blinks the built in LED on the Pi Pico, and then extends the blink by 1 second each loop

blinkTime = 1 #this sets variable to 1 second

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(blinkTime)
    led.value = False
    time.sleep(blinkTime)
    blinkTime += 1 #This increases the variable by 1 second each loop