#!/usr/bin/env python3
from ev3dev.ev3 import * as ev3

# Speak a message
ev3.Sound.speak('Welcome to the E V 3 dev project!').wait()
