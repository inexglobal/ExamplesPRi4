import RPi.GPIO as GPIO
import time
sw_pin = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
try :
  while 1:
    st_sw = GPIO.input(sw_pin)
    print("SW = " + str(st_sw))
    time.sleep(0.5)
finally :
  GPIO.cleanup()
