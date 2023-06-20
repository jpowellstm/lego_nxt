"""
Contained within are functions that allow a BBC Microbit to opperate the motors and sensors from a LEGO NXT robot kit.
"""

from microbit import *

# configure microbit
display.off()

# Define pin names
# Pins 5 and 11 are reserved for button input

# Motor 1
m1_1 = pin0
m1_2 = pin1
m1_enc1 = pin2
m1_enc2 = pin3

# Motor 2
m2_1 = pin4
m2_2 = pin6
m2_enc1 = pin7
m2_enc2 = pin8

def motor():
  """
  Turns to motor spinning in either direction
  """

def direction_control():
  """
  Reads the encoder on a motor, if outputs from two motors are different then 
  Connect the following wires: red - 0V, green - 5v, yellow - m1_enc1, blue - m1_enc2 
  """
  
  now = time.ticks_ms()
  scheduled_time = 100
  
  # Read start values of encoders
  o1_s = m1_enc1.read_digital():
  o2_s = m1_enc2.read_digital():
  o3_s = m2_enc1.read_digital():
  o4_s = m3_enc2.read_digital():
    
  # set counter variables
  count_1 = 0
  count_2 = 0
    
  while ticks_diff(scheduled_time, now) > 0:
    o1 = m1_enc1.read_digital():
    o2 = m1_enc2.read_digital():
    o3 = m2_enc1.read_digital():
    o4 = m3_enc2.read_digital():
      
    if o1 == o1_s and o2 == o2_s:
      count_1 += 1
      
    if o3 == o3_s and o4 == o4_s:
      count_2 += 1
     


# Run Loop
while True:
  # Read sensors
  
  if condition 1:
    state 1
  elif condition 2:
    state 2
  .
  .
  .
  
  
