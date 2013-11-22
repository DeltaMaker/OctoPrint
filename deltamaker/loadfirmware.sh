#!/bin/bash
# Script to load marlin from the Pi

avrdude -p m2560 -C /etc/avrdude.conf -c stk500v2 -P /dev/ttyUSB0 ~/OctoPrint/deltamaker/Marlin.cpp.hex
