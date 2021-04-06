from selenium import webdriver
from time import sleep

#Versión silenciosa
op = webdriver.ChromeOptions()
op.add_argument('headless')
#

driver = webdriver.Chrome('C:\EANT\EANT-PDP-0-MODELO\EANT-PDP-0-MODELO\Selenium\chromedriver.exe', options=op)

driver.get('https://www.cuspide.com/resultados.aspx?c=Biolog%C3%ADa,%20Ciencias%20de%20la%20Tierra(T%C3%A9cnicos)&tema=2173&por=Tema&orden=fecha&pg=1')

js_click_boton = """
    boton = document.querySelector('[title="Siguiente"]')
    if (boton){
            boton.click()
    }else{
        return "Fin Página"
    }
"""

from bs4 import BeautifulSoup

while driver.execute_script(js_click_boton) != "Fin Página":
    
    sleep(2)
    html = driver.execute_script("return document.documentElement.outerHTML")
    
    ####BeautifulSoup
    dom = BeautifulSoup(html, features='html.parser')
    
    articulos = dom.find_all(class_ ='libro libro')
    
    for articulo in articulos:
        titulo = articulo.a.get('title')
        precio = articulo.find(class_ ='precio').text
        print(titulo + " / " + precio)
        