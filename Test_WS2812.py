import time
import board
import neopixel
LED_COUNT      = 1     			# Number of LED pixels.
LED_PIN        = board.D12      # GPIO pin connected to the pixels (12 uses PWM!).
LED_BRIGHTNESS = 0.1      		# Set to 0 for darkest and 1 for brightest
pixels1 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS)

pixels1[0] = (255, 0, 0);time.sleep(1)
pixels1[0] = (0, 255, 0);time.sleep(1)
pixels1[0] = (0, 0, 255);time.sleep(1)
#LED to off
pixels1.fill((0, 0, 0))