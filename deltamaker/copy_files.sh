#!/bin/bash
# Script to setup the pi...

# Files to copy:
cd -f /home/pi/OctoPrint/deltamaker
# /home/pi/.octoprint/config.yaml
cp -f config.yaml /home/pi/.octoprint/config.yaml
# /home/pi/bin/octoprint
cp -f octoprint /home/pi/bin/octoprint

# /etc/rc.local
sudo cp -f rc.local /etc/rc.local
# /etc/haproxy/haproxy.cfg
sudo cp -f haproxy.cfg /etc/haproxy/haproxy.cfg
# /etc/default/haproxy
sudo cp -f haproxy /etc/default/haproxy
# /etc/hostname
sudo cp -f hostname /etc/hostname
# /etc/hosts
sudo cp -f hosts /etc/hosts
# /etc/hostapd/hostapd.conf
sudo cp -f hostapd.conf /etc/hostapd/hostapd.conf
# /etc/default/hostapd
sudo cp -f hostapd /etc/default/hostapd
