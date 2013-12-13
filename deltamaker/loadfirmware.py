#!/usr/bin/env python

import os
import subprocess

command = "cp /home/pi/OctoPrint/deltamaker/Marlin.cpp.hex /home/pi/Marlin.cpp.hex"
subprocess.call(command.split())

command = "sudo shutdown -r now"
subprocess.call(command.split())