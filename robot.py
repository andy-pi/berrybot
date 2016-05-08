import RPi.GPIO as GPIO
import time
from motor import straight, turn
# this module (motor) has two functions, turn("direction",time) and straight("direction",time)

GPIO.cleanup()
GPIO.setmode(GPIO. BCM)

TRIG=23
ECHO=24
SPEEDOFSOUND=34500 # incm/s

GPIO.setup(TRIG, GPIO. OUT)
GPIO.setup(ECHO, GPIO. IN)

GPIO.output(TRIG, False)
time.sleep(2)


def getdistance():
        pulse_start=0
        pulse_end=0

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO) == 0:
                pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
                pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * (SPEEDOFSOUND/2)
        distance = round(distance, 2)
        return distance
        print distance

while True:
        distance=getdistance()
        if (distance < 30):
                turn("left",0.22)
        else:
                straight("fwd",0.1)
