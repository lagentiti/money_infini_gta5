x = 716
y = 745
up = 6
click = 3

import time
import pydirectinput
import pyautogui
import random

while True:
    time.sleep(3)
    for i in range(up):
        pydirectinput.press("up")
        print("Up")
        time.sleep(random.uniform(0.5, 1))
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(1)
    for i in range(click):
        pydirectinput.mouseDown()
        time.sleep(random.uniform(0.1, 1))
        pydirectinput.mouseUp()
    print("click")
    time.sleep(random.uniform(40, 57))
