# Berry Bot

# Hardware
Raspberry Pi setup with wifi access.
Chassis with 2 indepedantly controllable motors
MotorHAT by UKonline2000 (http://ukonline2000.com/?p=775)
5V battery pack to power the pi
5V battery pack to power the motors
Jumper wires
Zip ties to hold things in place, and mounting screws for the pi

# Installation

SSH into your Pi and clone the repo. That's it!

``` bash
sudo git clone https://github.com/andy-pi/berrybot.git
```

# Python code walkthrough

## Sonar.py
This is simply a copy of a basic tutorial to use HC-SR04, and 