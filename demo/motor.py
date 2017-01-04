#!/usr/bin/env python3
from ev3dev.ev3 import *

# Run a motor

# Connect a large motor to output A

# Use variable 'm' to refer to the motor
m = ev3.LargeMotor('outA')

# Run the motor 'm' for 3000 ms and speed 500 ticks
m.run_timed(time_sp=3000, speed_sp=500)
