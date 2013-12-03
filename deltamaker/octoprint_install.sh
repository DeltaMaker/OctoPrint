#!/bin/bash
cd ~
sudo apt-get update
sudo apt-get install python-pip python-dev git
git clone https://github.com/DeltaMaker/OctoPrint.git
cd OctoPrint
sudo pip install -r requirements.txt
sudo usermod -a -G tty pi
sudo usermod -a -G dialout pi
