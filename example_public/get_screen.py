import time
import schedule

from PIL import ImageGrab

import pyautogui
import cv2 as cv
import numpy as np

def screen_grab():
    try:
        im = ImageGrab.grab()
        im.save("./temp/%d.png" % (time.time()), 'png')
    except Exception as e:
        print(e)

def screenshot():
    screen = pyautogui.screenshot()
    target = cv.cvtColor(np.asarray(screen), cv.COLOR_RGB2BGR)
    cv.imshow("screenshot", target)
    cv.resizeWindow("screenshot", 800, 600)

schedule.every(1).seconds.do(screen_grab)

while True:
    schedule.run_pending()
    screenshot()
    if (cv.waitKey(500) == 27):
        break
