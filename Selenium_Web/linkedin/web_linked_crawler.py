# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:13:04 2019

@author: everl
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from bs4 import BeautifulSoup

def login():

    driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
    driver.get('https://www.linkedin.com/uas/login?_l=pt')
    driver.maximize_window()
    
    txt = open('pass.txt', 'r')
    texto = txt.readlines()
    
    email = driver.find_element_by_xpath('//*[@id="username"]')
    email.send_keys('everluca@hotmail.com')
    
    time.sleep(1)
    
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(texto[0])
    
    login = driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')
    login.click()
    time.sleep(5)
    return driver

def procurar(driver, var):
    search = driver.find_element_by_xpath('//*[@id="ember31"]/input')
    search.send_keys(var)
    time.sleep(1)
    search.send_keys(u'\ue007')
    time.sleep(1)
    search.clear()
    pyautogui.click(1050,245, duration=3)
    pyautogui.click(987,403, duration=1)
    pyautogui.click(1323,573, duration=1)
    pyautogui.screenshot('scr.png')
    time.sleep(1)
    w, h = pyautogui.locateCenterOnScreen('eu.PNG')
    #w, h = pyautogui.locateCenterOnScreen('eu.PNG')
    time.sleep(1)
    pyautogui.moveTo(w, h,duration=3)
    return driver
    
def get_links(driver):
    #print(driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    #print(soup.prettify)
    
    for a in soup.find_all('a', class_='search-result__result-link ember-view'):
        print(a['href'])
        
driver = login()
driver = procurar(driver,'Hub inteligencia artificial Londrina')
get_links(driver)

time.sleep(2)
driver.close()

#class="distance-badge separator ember-view"