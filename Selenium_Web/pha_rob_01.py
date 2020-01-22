# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:26:05 2019

@author: everl
"""

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = r'C:\chromedriver_win32\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)