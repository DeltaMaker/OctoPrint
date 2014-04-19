#!/usr/bin/env python
# this script is run at boot to patch config.yaml or load firmware, if necessary

import os
import sys
import subprocess
import serial
import time

grep = "grep resetsettings.py /home/pi/.octoprint/config.yaml"
copycfg = "cp -b /home/pi/OctoPrint/deltamaker/config.yaml /home/pi/.octoprint"
restart = "sudo shutdown -r now"
command = "avrdude -p m2560 -c stk500v2 -P /dev/ttyUSB0 -U flash:w:/home/pi/Marlin.cpp.hex"
octoprint = "sudo -u pi /home/pi/bin/octoprint"

if subprocess.call(grep.split()) == 1: #must replace config.yaml file
    subprocess.call(copycfg.split())

def resetSerial():
    ser = serial.Serial("/dev/ttyUSB0")
    ser.setDTR(0)
    time.sleep(0.1)
    ser.setDTR(1)
    ser.close()
    time.sleep(4)

if os.path.exists("/home/pi/Marlin.cpp.hex"):
    resetSerial()
    if subprocess.call(command.split()) == 0:
        print("Update Successful!")
        os.remove("/home/pi/Marlin.cpp.hex")
        #subprocess.call(restart.split())

subprocess.call(octoprint.split())        
