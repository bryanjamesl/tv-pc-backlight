# inspiration from multiple sites, but started with https://www.youngwonks.com/blog/How-to-use-an-RGB-LED-with-the-Raspberry-Pi-Pico
# needed to invert the outputs since it is an common anode LED
# the button pushes were unpredictible, so pretty much all re-written with Bill.
# nany mods later.  Bill figured out it will work if I totally remove the resistor (which the leaves no current limiting).
# i added 24 Ohms to the anode, still works 
# Harrison almost complete re-write - works well!

from machine import Pin
from time import sleep_ms

# constants - # 24K ohms of restiors to 3.3v VCC (common anode RGB) 
led_r = Pin(18, Pin.OUT)                  # red lead on pin 20 
led_g = Pin(19, Pin.OUT)                  # green on pin 19
led_b = Pin(20, Pin.OUT)                  # blue on pin 18
switch = Pin(27, Pin.IN, Pin.PULL_DOWN) # switch on pin 27 using internal pull down

# r, g, b - each color state is inverted to accomidate the common anode LED
colors = [
  (1, 1, 0), # blue
  (0, 1, 1), # red
  (1, 0, 1), # green
  (0, 0, 1), # yellow
  (0, 1, 0), # magenta
  (1, 0, 0), # cyan
]

# state variables
cur_color = 0 # index of current color

def set_color(color):
  """
  Sets the color of the RGB LED based on the input color tuple.

  Args:
      color (tuple): A tuple representing the RGB values to set. Each value should be in the range of 0 to 1.

  Returns:
      None
  """
  led_r.value(color[0])
  led_g.value(color[1])
  led_b.value(color[2])

def set_next_color():
  """
  Increment the current color index and set the next color based on the updated index.
  """
  global cur_color
  cur_color = (cur_color + 1) % len(colors) # modulo to allow additional colors to be added
  set_color(colors[cur_color])              # set the color using the "list" parameters 

def debounce():                             # Debounce circuit (BH)
  switch_up_time = 0
  time_limit = 2000
  sleep_ms(100)
  while True:
    if switch.value() == 0:                 # When switch "indicates" open
      switch_up_time +=1
    else:
      switch_up_time = 0
    if switch_up_time > time_limit:
      return

set_color((1, 1, 1))                        # turn all LEDs off to start
sleep_ms(500)                               # all off for 500ms
set_color(colors[0])                        # set to the first color

while True:
  if switch.value() == 1:                   # switch is pressed
    set_next_color()                        # wait for the switch to be released
    debounce()