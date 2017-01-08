#!/usr/bin/env python3

import logging
from TRACK3R import TRACK3RWithHammer

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)

log.info("Starting TRACK3RWithHammer")
tracker = TRACK3RWithHammer()
tracker.main()
log.info("Exiting TRACK3RWithHammer")
