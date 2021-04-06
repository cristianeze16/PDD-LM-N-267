# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:04:10 2021

@author: crist
"""
from bs4 import BeautifulSoup # libreria scraping Toma el texto HTML y lo analiza 

archivo_html = open('web_ejemplo.html',encoding= 'utf-8')

dom = BeautifulSoup(archivo_html, features='html.parser')


# print(dom.prettify())
# Metodos de captura 

primer_link = dom.a
print(primer_link.string)

primer_link = dom.find('a')

todos_los_links = dom.find_all('a')

# capturando los valores delos atributo

print(primer_link['class'])
print(primer_link['href'])
print(primer_link['id'])

