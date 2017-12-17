#Source: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

#Library needed for RaspberryPi Camera
from picamera import PiCamera
from time import sleep

NUM_PICTURES = 5
SLEEP_TIME = 50/100 

camera = PiCamera()

for i in range(NUM_PICTURES):
    camera.start_preview()
    sleep(SLEEP_TIME)
    #Used to take a still picture
    picture = ('test' + str(i) + '.jpg')	
    camera.capture(picture)

    camera.stop_preview()
