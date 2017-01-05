#!/usr/bin/env python3
import ev3dev.ev3 as ev3

# Variable 'ts' refers to the touch sensor (make sure it is connected)
ts = ev3.TouchSensor()

# Run the loop forever
while True:
  # Sets the Left LED to change from Green to Red when the touch sensor is pressed
  ev3.Leds.set_color(ev3.Leds.LEFT, (ev3.Leds.GREEN, ev3.Leds.RED)[ts.value()])
  
# Use Ctrl-C to exit
