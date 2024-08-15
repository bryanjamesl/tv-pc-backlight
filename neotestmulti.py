import time
import machine, neopixel
# from neopixel import NeoPixel as NP
npPin = machine.Pin(23, machine.Pin.OUT)
np = neopixel.NeoPixel(npPin, 1)
slp = 50

def demo(np):
    n = np.n

    np[0] = (0, 0, 0)
    time.sleep(1)

    print("in loop")
    for i in range(0, 250):
        np[0] = (0, i, 255)
        np.write()
        time.sleep_ms(slp)   
    for i in range(255, 0):
        np[0] = (0, i, 255)
        time.sleep_ms(slp)

    #np[0] = (0, 0, 0)
    for i in range(0, 255):
        np[0] = (i, 100, 0)
        np.write()
        time.sleep_ms(slp)   

    #np[0] = (0, 0, 0)
    for i in range(0, 255):
        np[0] = (244, 0, i)
        np.write()
        time.sleep_ms(slp)   

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
