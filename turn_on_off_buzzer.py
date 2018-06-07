#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32

GPIO.setup(buzz_pin, GPIO.OUT)

Buzz = GPIO.PWM(buzz_pin, 1000)

def buzz(freq, time_taken):
	Buzz.ChangeFrequency(freq)
	Buzz.start(50)
	time.sleep(time_taken)
	Buzz.stop()

buzz(440, 1)
buzz(880, 2)

GPIO.cleanup()
