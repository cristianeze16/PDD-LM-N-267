# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 17:19:33 2021

@author: crist
"""

archivo_entrada = open('peliculas/peliculas.csv',encoding='utf-8')
archivo_salida = open('peliculas/peliculas_ordenado.csv','w',encoding= 'utf-8')
for linea in archivo_entrada:
    linea = linea.replace('\n','')
    lista = linea.split('"')
    lista = linea.split(',')
    # print(lista[0],lista[1],lista[2])
    archivo_salida.write(lista[0] +',' + lista[1] + ',' + lista[2] + '\n')
archivo_entrada.close()
archivo_salida.close()
 