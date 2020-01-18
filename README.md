# Web_Crawling  
```
#geckdriver = 'geckodriver'
from selenium import webdriver
driver = webdriver.Firefox()
import time

driver.get('http://www.google.com')
#inputs = driver.find_elements_by_tag_name('img')
inputs = driver.find_element_by_name('q')
#for elem in inputs: 
#       print(elem.get_attribute('outerHTML'))
#html = inputs[0].get_attribute('outerHTML')
#print(html)
inputs.send_keys('Willian Shakes')
time.sleep(5)
inputs.send_keys(u'\ue007')
```
## Docs
### https://selenium-python.readthedocs.io/locating-elements.html
  
from selenium import webdriver
driver = webdriver.Firefox()
import time

driver.get('https://stopots.com.br/1360')
time.sleep(5)
btn_entrar = driver.find_elements_by_class_name('enter')[0]

btn_entrar.send_keys(u'\ue007')

time.sleep(20)
btn_entrar = driver.find_elements_by_class_name('icon-exclamation')[0]

btn_entrar.send_keys(u'\ue007')
time.sleep(10)
soup_letra = driver.find_element_by_id('letter')
letra = soup_letra.find_elements_by_tag_name('span')[0].text
fild_n = driver.find_elements_by_class('')
fild_n.send_keys(letra)
print(letra)

---------------------------------------------------------------

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:12:14 2019

@author: root
"""

#!/root/miniconda3/envs/env01/bin/python

from selenium import webdriver

#time.sleep(5)
#btn_entrar = driver.find_elements_by_class_name('enter')[0]
#btn_entrar.send_keys(u'\ue007')

#time.sleep(20)
#btn_entrar = driver.find_elements_by_class_name('icon-exclamation')[0]

#btn_entrar.send_keys(u'\ue007')
#time.sleep(10)
tema = []
valores = []
validados = []
i=0
while i < 10:
    print('Tentando novamente')
    try:
        btn_avaliar = driver.find_elements_by_class_name('icon-exclamation')[0].text
    #print(btn_avaliar)
    except:
        pass
    if btn_avaliar == 'AVALIAR':
        try:
            fields = driver.find_elements_by_tag_name('label')
            campo = driver.find_elements_by_class_name('validation')[0]
            campo = campo.find_elements_by_tag_name('div')[0].text
            campo = campo.split(':')[1].split('\n')[0].strip()
            print(campo)
            for field in fields:
                valor = field.find_elements_by_tag_name('div')[0].text
                print(valor)
                status = field.find_elements_by_tag_name('span')[0].text
                print(status)
                #campo.send_keys(10*letra)
                tema.append(campo)
                valores.append(valor)
                validados.append(status)
        except:
            pass
        
    time.sleep(5)
    i+=1
    
    ---------------------------------------------------------------------------------------------------
    
    #!/root/miniconda3/envs/env01/bin/python

from selenium import webdriver
driver = webdriver.Firefox()
import time

driver.get('https://stopots.com.br/13918')

time.sleep(5)
btn_entrar = driver.find_elements_by_class_name('enter')[0]
btn_entrar.send_keys(u'\ue007')

time.sleep(20)
btn_entrar = driver.find_elements_by_class_name('icon-exclamation')[0]

btn_entrar.send_keys(u'\ue007')
time.sleep(10)
soup_letra = driver.find_element_by_id('letter')
letra = soup_letra.find_elements_by_tag_name('span')[0].text
#fild_n = driver.find_elements_by_class('')
#fild_n.send_keys(letra)
print(letra)

fields = driver.find_elements_by_tag_name('label')
for field in fields:
    try:
        campo = field.find_elements_by_tag_name('span')[0].text
        print(campo)
        campo = field.find_elements_by_tag_name('input')[0]
        campo.send_keys(10*letra)
    except:
        pass
    
