import requests
import pprint
import json
from selenium import webdriver



key = 'f4d0c0500a7273fae7a630dc72abd6bb'
archivo_in = open('sucursales_sol_360.csv')
log_error = open('sol360_log_error.txt','w')


for linea in archivo_in:
    linea = linea.split(';')
    print(linea[0])
    ciudad_cod = requests.utils.quote(linea[0])
    provincia_cod = requests.utils.quote(linea[1])
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+ciudad_cod+',Argentina&lang=es&appid='+ key
    objeto = json.loads(requests.get(url).text)
    descripcion = objeto.get('weather')
    if objeto.get('weather') == None:
        log_error.write(linea[0] + " no encontrada\n")
    else:
        print(linea[0],'->',objeto.get('weather')[0]['description'])
    
    
    
    
    
log_error.close()