#!/usr/bin/env python3
'''
Demonstrate different operations and info about motors
'''

import ev3dev.ev3 as ev3
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)

log.info("Starting Motor Demo")

m = ev3.LargeMotor(OUTPUT_A)

def logMotor:
  log.info(m.address())
  log.info(m.commands())
  log.info(m.count_per_rot())
  log.info(m.count_per_m())
  log.info(m.duty_cycle())
  log.info(m.full_travel_count())
  log.info(m.polarity())
  log.info(m.position())
  log.info(m.max_speed())
  log.info(m.speed())
  log.info(m.state())
  return
  
logMotor()
