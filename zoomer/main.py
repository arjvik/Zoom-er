import numpy as np
from itertools import cycle
from time import sleep
from timer import Timer
from pyfakewebcam import FakeWebcam
from cv2 import VideoCapture

cam = FakeWebcam('/dev/video4', 640, 480)

while True:
    video = VideoCapture('test-resized.mp4')
    while (read := video.read())[0]:
        with Timer("Scheduling frame", verbose=True):
            cam.schedule_frame(read[1][:,:,::-1])
        sleep(1/60)