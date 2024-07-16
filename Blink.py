import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
while 1:
  GPIO.output(5,1)
  time.sleep(0.5)
  GPIO.output(5,0)
  time.sleep(0.5)
