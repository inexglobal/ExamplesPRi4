import datetime
from PIL import ImageFont
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from time import sleep

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

font_path = "/home/pi101/Desktop/ExamplesPRi4/fonts/THSarabun.ttf"
font2 = ImageFont.truetype(font_path, 24)

last_sec=0
while 1:
    datenow=datetime.datetime.now()
    if datenow.second!=last_sec:
        str_weekday=datenow.strftime("%A")
        str_date=datenow.strftime("%d/%m/%Y")
        str_time=datenow.strftime("%H:%M:%S")
        last_sec=datenow.second
        print(datenow.strftime("%A : %d/%m/%Y , %H:%M:%S"))
        with canvas(device) as draw:
            draw.text((0, 0),str_weekday,font=font2, fill=1)
            draw.text((0, 18),str_time,font=font2, fill=1)
            draw.text((0, 40),str_date,font=font2, fill=1)


