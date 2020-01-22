# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:55:37 2019

@author: everl
"""

import pyautogui

pyautogui.screenshot('scr.png')
pyautogui.locateOnScreen('eu.PNG')
w, h = pyautogui.locateCenterOnScreen('eu.PNG')
pyautogui.moveTo(w,h,duration=3)