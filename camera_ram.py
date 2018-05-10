#Source: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

#Library needed for RaspberryPi Camera
from picamera import PiCamera
from time import *
import signal
import sys
import io

NUM_PICTURES = 5
SLEEP_TIME = 50/100 

my_stream = io.BytesIO()

def signal_handler(signal,frame):
    print("loop: " + str(sum(loop)/len(loop)))
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

camera = PiCamera()

lstart = 0
lstop  = 0
loop = []
picture = ('/ram/test.jpg')

while True:

    #Used to take a still picture
    print("Start Capture")
    lstart = time()
    camera.capture(picture)
    lstop = time()
    print("End Capture")
    loop.append(lstop - lstart)
