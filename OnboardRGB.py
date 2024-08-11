# misc different code from internet.  I've not been able to get it to work 7-23-24

import time
import machine, neopixel
# from neopixel import NeoPixel as NP
npPin = machine.Pin(23, machine.Pin.OUT)
np = neopixel.NeoPixel(npPin, 3)

def demo(np):
    n = np.n
 
    # cycle
    print("in cycle")
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (0, 75, 0)
        np.write()
        time.sleep_ms(225) #original code is 25

    # bounce
    print("in bounce")
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(260) #original code is 60

    # fade in/out
    print("in fade")
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()
        time.sleep_ms(40)

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
    time.sleep_ms(1000)

while True:
    demo(np)


"""

from neopixel import NeoPixel, pixels.colorHSV
from time import sleep

## Setup
NUM_LEDS = 1
LED_PIN = 23
pixels = NeoPixel(NUM_LEDS, 0, LED_PIN, "GRB")

## Constants
red = pixels.colorHSV(0, 255, 255)
green = pixels.colorHSV(21845, 255, 255)
blue = pixels.colorHSV(43691, 255, 255)

## Loop
while True:
  for hue in range(0, 65535, 500):
    color = pixels.colorHSV(hue, 255, 255)
    pixels.fill(color)
    pixels.show()
    sleep(0.05)

"""


""" 



while True:
    demo(np)




from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

npPin = Pin(23, Pin.OUT)
np = NeoPixel(npPin, 1)

while True:
    np[0] = (255, 0, 0)
    np.write()
    sleep_ms(4000)

    np[0] = (0, 255, 0)
    np.write()
    sleep_ms(4000)

    np[0] = (0, 0, 255)
    np.write()
    sleep_ms(4000)



Written w/BH to test onboard neopixel
from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

npPin = Pin(23, Pin.OUT)
np = NeoPixel(npPin, 1)

while True:
    np[0] = (255, 0, 0)
    np.write()
    sleep_ms(4000)

    np[0] = (0, 255, 0)
    np.write()
    sleep_ms(4000)

    np[0] = (0, 0, 255)
    np.write()
    sleep_ms(4000)


import machine, neopixel 

np = neopixel.NeoPixel(machine.Pin(23), 3)

np[0] = (255, 0, 0) # set to red, full brightness
np[1] = (0, 128, 0) # set to green, half brightness
np[2] = (0, 0, 64)  # set to blue, quarter brightness


import neopixel
from machine import Pin
import time

ws_pin = 23
led_num = 1
BRIGHTNESS = 0.5  # Adjust the brightness (0.0 - 1.0)

neoPix = neopixel.NeoPixel(Pin(ws_pin), led_num)

def set_brightness(color):
    r, g, b = color
    r = int(r * BRIGHTNESS)
    g = int(g * BRIGHTNESS)
    b = int(b * BRIGHTNESS)
    return (r, g, b)

def loop():
    # Display red
    color = (255, 0, 0)  # Red color
    color = set_brightness(color)
    neoPix.fill(color)
    neoPix.write()
#    neoRing.fill(color)
#    neoRing.write()
    time.sleep(1)
    print("in red")

    # Display green
    color = (0, 255, 0)  # Green color
    color = set_brightness(color)
    neoPix.fill(color)
    neoPix.write()
    time.sleep(1)
    print("in green function")

    # Display blue
    color = (0, 0, 255)  # Blue color
    color = set_brightness(color)
    neoPix.fill(color)
    neoPix.write()
    time.sleep(1)
    print("in blue")

while True:
    loop()



import neopixel, machine

# 32 LED strip connected to X8.
p = machine.Pin(23)
n = neopixel.NeoPixel(p, 1)
# led_r = Pin(23, Pin.OUT)

# Draw a red gradient.
for i in range(1):
    n[i] = (i * 8, 0, 0)

# Update the strip.
n.write()

"""

