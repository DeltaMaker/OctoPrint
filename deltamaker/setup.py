#!/usr/bin/env python
# Script to setup the pi...

import os
import subprocess
import sys

os.chdir("/home/pi/OctoPrint")

command = "git pull"
if subprocess.call(command.split()) == 1: #Exit status 1 is failure.
    sys.exit(1) #Pass that failure along to Octoprint.

command = "sudo pip install -r requirements.txt"
subprocess.call(command.split())
sys.exit(0)

#cd ~/OctoPrint && git pull && sudo pip install -r requirements.txt