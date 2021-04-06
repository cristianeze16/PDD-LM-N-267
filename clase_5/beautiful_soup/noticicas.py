# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:04:10 2021

@author: crist
"""
from bs4 import BeautifulSoup
import requests


url = "https://www.ambito.com/"
response = requests.get(url)
response.encoding = 'utf-8'
archivo_html = response.text

dom = BeautifulSoup(archivo_html, features = 'html.parser')
noticias = dom.find_all(class_='title')

for link in noticias:
    
    target_noticias = link.a
    print(target_noticias['href'])
    
    


