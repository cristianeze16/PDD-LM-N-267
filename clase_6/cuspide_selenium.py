# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:07:18 2021

@author: crist
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
driver = webdriver.Chrome('./chromedriver.exe')


driver.get ('https://www.cuspide.com/resultados.aspx?c=Biolog%c3%ada%2c+Ciencias+de+la+Tierra(T%c3%a9cnicos)&tema=2173&por=Tema&orden=fecha')

# js_clickear_boton = """
#                 boton = document.querySelector('[data-aut-id="btnLoadMore" ]')
#                 boton.click()
                
# """

js_click_boton = """
                boton = document.querySelector('[id = "ctl00_ContentPlaceHolder1_PagerControl2_lnkSiguiente"]')
                if(boton){
                      boton.click()
                        
                        }else{
                            return "FIN"
                            }
"""

while  driver.execute_script(js_click_boton)!= "FIN":
    sleep(5)
    html = driver.execute_script("return document.documentElement.outerHTML")
    
    dom = BeautifulSoup(html,features ='html.parser')
    
    articulos = dom.find_all(class_ = 'libro libro')
    
    for articulo in articulos:
        titulo = articulo.a.get('title')
        precio = articulo.find(class_ = 'precio').text
        print(titulo +"/" + precio)