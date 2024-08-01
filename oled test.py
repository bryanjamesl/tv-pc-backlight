import time														# import time
from machine import Pin, I2C									# import I2C protocol
from ssd1306 import SSD1306_I2C									# import OLED SSD1306

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
devices = i2c.scan()
TempSensor = machine.ADC(4)
oled = SSD1306_I2C(128, 64, i2c,addr=devices[0])
sum4avg = 0														# stores total for average temp over time
averageT = 0 													# var for average temp, total divided by number of samples

while True:
    oled.fill(0)												# to blank the screen
    oled.text("hello world", 0, 0)								# confirming the display is working
    data = TempSensor.read_u16() * 3.3 / 65535					# read the sensor adc output
    sum4avg = 0
    
    for x in range(0, 5):										# average 5 readings
        temperature = 27-(data-0.706)/0.001721					# calculate C (
        sum4avg = temperature + sum4avg
        print("sum ",sum4avg)	# debug
        print(temperature)		# debug
        time.sleep(1)
    averageT = sum4avg / 5 + 1.5# temp average. I ADDED 1.5 to compensate for the error, probably due to the Vref
    print(" Avg ",averageT)		# debug
    
    oled.text("Temperature: ", 0, 15)							# print temperature
    oled.text(str(round(averageT,1)),0,33)						# print C
    oled.text("C",44,33)
    
    oled.text(str(round((9/5*averageT+32),1)),0,50)				# print temperature F
    oled.text("F", 44, 50)										# print F
    oled.show()
   
    


