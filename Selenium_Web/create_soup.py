# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:45:55 2019

@author: everl
"""

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path = r'C:\chromedriver_win32\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.prettify())

driver.quit()