import RPi.GPIO as GPIO
import time
sw_pin_up=6
sw_pin_down=23
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw_pin_up,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw_pin_down,GPIO.IN,pull_up_down=GPIO.PUD_UP)
try :
  while 1:
    st_sw_up = GPIO.input(sw_pin_up)
    st_sw_down = GPIO.input(sw_pin_down)
    if st_sw_up == 0:
        count += 1
        print("Count = %d " % count);time.sleep(0.2)
    if st_sw_down == 0:
        count -= 1
        print("Count = %d " % count);time.sleep(0.2)
finally :
  GPIO.cleanup()