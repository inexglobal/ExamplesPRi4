from PIL import ImageFont
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from time import sleep

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

font_path = "/home/pi101/Desktop/ExamplesRPi4/fonts/THSarabun.ttf"
font2 = ImageFont.truetype(font_path, 24)

with canvas(device) as draw:
    draw.text((0, 0), "Hello World",font=font2, fill="white")
    draw.text((0, 30), "สวัสดีชาวโลก",font=font2, fill="white")
sleep(5)
