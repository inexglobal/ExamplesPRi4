import RPi.GPIO as GPIO
import time
sw_pin=13
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
try :
  while 1:
    st_sw = GPIO.input(sw_pin)
    if st_sw == 0:
      count += 1
      print("Count = %d " % count)
      time.sleep(0.2)
finally :
  GPIO.cleanup()
