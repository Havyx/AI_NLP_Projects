# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:19:03 2019

@author: everl
"""

import pyautogui
print(pyautogui.size())
tam, alt = pyautogui.size()

position = pyautogui.position()
print(position)

pyautogui.moveTo(100,100, duration=1)
pyautogui.moveRel(200, 0, duration=3)
pyautogui.moveRel(0, -100, duration=3)
pyautogui.click(100,100, duration=3)
