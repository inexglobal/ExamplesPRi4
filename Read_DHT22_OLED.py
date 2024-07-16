from PIL import ImageFont
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from time import sleep
import datetime

import RPi.GPIO as GPIO
from DHT_Python import dht22
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

msgTime = ""
msgTemp = ""
msgHumi = ""
# read data using pin 4 instance
instance = dht22.DHT22(pin=4)

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

font_path = "/home/pi101/Desktop/ExamplesPRi4/fonts/THSarabun.ttf"
font2 = ImageFont.truetype(font_path, 24)
last_sec=0
while True:
    datenow=datetime.datetime.now()
    if datenow.second!=last_sec:
        result = instance.read()
        msgTime=datenow.strftime("%H:%M:%S")
        if result.is_valid():
            msgTemp="T : %.1f °C" % result.temperature
            msgHumi="H : %.1f %%" % result.humidity
        sleep(1)
        with canvas(device) as draw:
            draw.text((0, 0), msgTime,font=font2, fill="white")
            draw.text((0, 20), msgTemp,font=font2, fill="white")
            draw.text((0, 40), msgHumi,font=font2, fill="white")
