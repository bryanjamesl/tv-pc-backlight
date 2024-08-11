import time
import machine, neopixel
# from neopixel import NeoPixel as NP
npPin = machine.Pin(23, machine.Pin.OUT)
np = neopixel.NeoPixel(npPin, 1)

def demo(np):
    n = np.n

    np[0] = (0, 0, 0)
    time.sleep(1)

    # cycle
   # print("in loop")
   # for i in range(0, 250):
   #     np[0] = (0, 175, i)
   #     np.write()
   #     time.sleep_ms(10)   

    np[0] = (0, 0, 0)
    for i in range(0, 255):
        np[0] = (i, 100, 0)
        np.write()
        time.sleep_ms(10)   

    np[0] = (0, 0, 0)
    for i in range(0, 255):
        np[0] = (i, 0, 200)
        np.write()
        time.sleep_ms(10)   

while True:
    demo(np)


"""

"""
"""
def demo2(np):
    print("in 2nd loop")
    n = np.n
    for k in range(0, 150):
        for i in range(0, 150):
            for j in range(n):
                np[0] = (0, 0, 0)
        np[0] = (150, i, k)
        np.write()
        time.sleep_ms(50)   

"""
