# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:00:12 2021

@author: crist
"""

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://es.wikipedia.org/wiki/MacOS#Versiones')