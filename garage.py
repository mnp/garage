#!/usr/bin/python

from bottle import route, run, template
from time import sleep
import RPi.GPIO as GPIO
import atexit
import logging

# left bay, as looking from driveway
GARAGE_L_IN   = 35 
GARAGE_L_OUT  = 38

# right bay, as looking from driveway
GARAGE_R_IN  = 37
GARAGE_R_OUT = 40

BOUNCETIME = 200

inputs  = [GARAGE_L_IN, GARAGE_R_IN]
outputs = [GARAGE_L_OUT, GARAGE_R_OUT]
changed = 0

@atexit.register
def cleanup():
    '''Make sure we leave the relays de-energized'''
    logging.info("cleaning up")
    GPIO.output(outputs, GPIO.HIGH)
    GPIO.cleanup()
    logging.info("cleanup finished")

def niceState(channel):
    if GPIO.input(channel):
        return ("label-success", "DOWN")
    else:
        return ("label-warning", "UP")

def showstate(msg):
    for i in inputs:
	logging.info("{} - pin {} state {}".format(msg, i, GPIO.input(i)))

def changing(channel):
	global changed
	logging.info("channel {} changed to {}".format(channel, GPIO.input(channel)))
	changed = 1

def changeloop():
    global changed
    while True:
	sleep(1)
	if changed:
	    showstate("changed")
	    changed = 0

def makeRoot(message):
    (lc, ls) = niceState(GARAGE_L_IN)
    (rc, rs) = niceState(GARAGE_R_IN)
    return template("garage.tpl", message=message, 
                    lclass=lc, rclass=rc, lstate=ls, rstate=rs,
                    lchan=GARAGE_L_OUT, rchan=GARAGE_R_OUT)

@route("/")
def root():
    return makeRoot("")

@route("/pulse/<channel>")
def pulse_output(channel):
    cnum = int(channel)
    logging.info("Pulsing output {}".format(cnum))
    GPIO.output(cnum, False)
    sleep(1)
    GPIO.output(cnum, True)
    return makeRoot("Pulsed " + channel)

logging.basicConfig(format="%(asctime)-15s %(message)s", level=logging.INFO,
                    filename="/var/log/garage.log")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GARAGE_L_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GARAGE_R_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GARAGE_L_OUT, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(GARAGE_R_OUT, GPIO.OUT, initial=GPIO.HIGH)
GPIO.add_event_detect(GARAGE_R_IN, GPIO.BOTH, callback=changing, bouncetime=BOUNCETIME)
GPIO.add_event_detect(GARAGE_L_IN, GPIO.BOTH, callback=changing, bouncetime=BOUNCETIME)

showstate("waking up")
sleep(2)
run(host='0.0.0.0', port=8888)
