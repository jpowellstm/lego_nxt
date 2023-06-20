"""
Contained within are functions that allow a BBC Microbit to opperate the motors and sensors from a LEGO NXT robot kit.
"""

from microbit import *

# configure microbit
display.off()

# Define pin names
# Pins 5 and 11 are reserved for button input

m1_1 = pin0
m1_2 = pin1
m1_enc1 = pin2
m1_enc2 = pin3


def motor():
  """
  Turns to motor spinning in either direction
  """

def encoder():
  """
  Reads the encoder on a motor
  Connect the following wires: red - 0V, green - 5v, yellow - m1_enc1, blue - m1_enc2 
  """
  m1_enc1.read_digital():
  m1_enc2.read_digital():
  
