#!/usr/bin/python
# Title:        intermediate function for using UKonline2000's motorHat
# Author:       AndyPi

from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
        mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
        mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
        mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
        mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

#################################

rMotor = mh.getMotor(4)
lMotor = mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)

def turn(dir,sec):
        rMotor.setSpeed(100)
        lMotor.setSpeed(100)
        if (dir=="left"):
                lMotor.run(Raspi_MotorHAT.BACKWARD)
        else:
                rMotor.run(Raspi_MotorHAT.BACKWARD)

        time.sleep(sec)
        rMotor.run(Raspi_MotorHAT.RELEASE)
        lMotor.run(Raspi_MotorHAT.RELEASE)

def straight(dir,sec):
        rMotor.setSpeed(105)
        lMotor.setSpeed(100)
        if (dir=="fwd"):
                rMotor.run(Raspi_MotorHAT.FORWARD)
                lMotor.run(Raspi_MotorHAT.FORWARD)
        else:
                rMotor.run(Raspi_MotorHAT.BACKWARD)
                lMotor.run(Raspi_MotorHAT.BACKWARD)
        time.sleep(sec)
        rMotor.run(Raspi_MotorHAT.RELEASE)
        lMotor.run(Raspi_MotorHAT.RELEASE)
