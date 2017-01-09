#!/usr/bin/env python3
'''
Demonstrate different operations and info about motors
'''

import ev3dev.ev3 as ev3
import logging
from time import sleep

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)

def logMotor(motor, log):
  log.info("===================")
  log.info("Current motor state")
  log.info(motor.address())
  log.info(motor.commands())
  log.info(motor.count_per_rot())
  log.info(motor.count_per_m())
  log.info(motor.duty_cycle())
  log.info(motor.full_travel_count())
  log.info(motor.polarity())
  log.info(motor.position())
  log.info(motor.max_speed())
  log.info(motor.speed())
  log.info(motor.state())
  log.info("Press any button to continue ...")
  while not btn.any():
    sleep(0.01)
  return

log.info("Starting Motor Demo")
btn = ev3.Button() # initialise button
m = ev3.LargeMotor('outA') # initialise motor
logMotor(m, log)

log.info("Resetting the motor")
m.reset()
logMotor(m, log)

motor_speed=100
motor_runtime=3000
log.info("Running for " + str(motor_runtime) + "ms and speed " + str(motor_speed))
m.speed_sp(motor_speed)
m.time_sp(motor_runtime)
m.run_timed()
logMotor(m, log)
