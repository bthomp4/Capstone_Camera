#Source: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

#Library needed for RaspberryPi Camera
from picamera import PiCamera
from time import sleep

camera = PiCamera()


for i in range(5):
    camera.start_preview()
    sleep(5)
    #Used to take a still picture
    camera.capture('test' + str(i) + '.jpg')
    camera.stop_preview()
