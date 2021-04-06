# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:26:05 2021

@author: crist
"""

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

driver.get ('https://www.olx.com.ar/items/q-aspiradora-para-autos')

# js_clickear_boton = """
#                 boton = document.querySelector('[data-aut-id="btnLoadMore" ]')
#                 boton.click()
                
# """


js_preguntar_boton = """
                boton = document.querySelector('[data-aut-id="btnLoadMore" ]')
                if(boton){
                       return "Existe"
                        
                        }else{
                            return "No existe"
                            }
"""
existe_boton = driver.execute_script(js_preguntar_boton)

while existe_boton == 'Existe':
    driver.execute_script(js_clickear_boton)
    sleep(5)
html =  existe_boton = driver.execute_script("return document.documentElement.outerHTML")
                                         
                                         
from bs4 import BeautifulSoup

dom = BeautifulSoup(html,features ='html.parser')

articulos = dom.find_all(class_ = 'IKo3_')

articulo = articulos[0]
for articulo in articulos:
    precio = articulo.find(class_ = '_89yzn').text
    titulo = articulo.find(class_ = '_2tW1I').
    
    print ()

