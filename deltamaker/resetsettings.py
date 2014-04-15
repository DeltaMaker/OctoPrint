#!/usr/bin/env python

import os
import subprocess

command = "cp /home/pi/OctoPrint/deltamaker/config.yaml /home/pi/.octoprint/config.yaml"
subprocess.call(command.split())

command = "/home/pi/OctoPrint/run --daemon restart"
subprocess.call(command.split())