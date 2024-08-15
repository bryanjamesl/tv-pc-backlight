# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/7
# added the two other colors (green and blue in this case)

from machine import Pin, PWM
from time import sleep, sleep_us

pwm_r = PWM(Pin(18)) 
pwm_g = PWM(Pin(20))
pwm_b = PWM(Pin(21))
pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)
delay_us = 1000

while True:
  for duty in range(65025, 0, -1):
    pwm_r.duty_u16(duty)
    sleep_us(delay_us)
  for duty in range(65025):
    pwm_r.duty_u16(duty)
    sleep_us(delay_us)
  for duty in range(65025, 0, -1):
    pwm_g.duty_u16(duty)
    sleep_us(delay_us)
  for duty in range(65025):
    pwm_g.duty_u16(duty)
    sleep_us(delay_us)
  for duty in range(65025, 0, -1):
    pwm_b.duty_u16(duty)
    sleep_us(delay_us)
  for duty in range(65025):
    pwm_b.duty_u16(duty)
    sleep_us(delay_us)  
