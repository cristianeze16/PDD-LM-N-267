from selenium import webdriver
from time import sleep
import json 


#Versión silenciosa
op = webdriver.ChromeOptions()
op.add_argument('headless')
#

driver = webdriver.Chrome('./chromedriver.exe', options=op)

driver.get('https://www.cuspide.com/resultados.aspx?c=Biolog%C3%ADa,%20Ciencias%20de%20la%20Tierra(T%C3%A9cnicos)&tema=2173&por=Tema&orden=fecha&pg=1')

precios = []
titulos = []




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
        precio_fil = precio.replace('\nAR$','AR$')
        precio_fil_1 = precio_fil.replace('\n                    ','')
        titulos.append(titulo)
        # precios.append(precio_fil_1)
       
        
        print(precios)
        objeto = {'precio':precios_fil_1,
                  'titulos':titulos
                  }
      
       
        
        with open('libros.json','w',encoding = 'utf-8') as archivoJson:
            json.dump(objeto,archivoJson, indent = 3)
        
        