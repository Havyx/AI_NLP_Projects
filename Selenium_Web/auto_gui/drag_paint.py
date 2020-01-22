# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:27:39 2019

@author: everl
"""

import pyautogui
import time

time.sleep(5)

pyautogui.click()
distance = 200

while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=1)
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=1)
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=1)
    distance = distance - 25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=1)