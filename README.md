# Hardware

## Items
Raspberry Pi setup with wifi access  
Chassis with 2 indepedantly controllable motors  
MotorHAT by UKonline2000 (http://ukonline2000.com/?p=775)  
7.2V battery pack to power the motors  
5V battery pack to power the pi    
Jumper wires  
Zip ties to hold things in place, and mounting screws for the pi  

## Connections
MotorHAT plugged into RaspberryPi GPIO  
7.2v battery pack connected to MotorHAT power terminals  
Motors wires to MotorHAT terminals 
(you'll need to test the software to see if it is the correct polarity, but if it is incorrect this only means the direction will be reverse)  
HC-SR04 ultrasonic sensor connected to Pi as follows:  
SENSOR   >   PI GPIO  
TRIG     >   23  
ECHO     >   24**  
VCC      >   5 volts  
GND      >   GND  

** Connected via a voltage divider to bring the input to the Pi down to 3.3v. This is because the Pi GPIO's work at 3.3v but the HC-SR04 is 5v. See [this tutorial](https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi) for full explanation  

# Software

SSH into your Pi and clone the repo. Then, just run the robot.py file and off you go! Press CTRL-C to stop.

``` bash
sudo git clone https://github.com/andy-pi/berrybot.git
cd berrybot
sudo python robot.py
```

# Python code walkthrough

See the details here: http://andypi.co.uk/2016/05/08/berry-bot/