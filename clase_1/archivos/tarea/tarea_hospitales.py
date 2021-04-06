

archivo_entrada = open('hospitales/hospitales.csv', encoding = 'utf-8')
archivo_salida = open('hospitales/hospitales_mod.csv', 'w', encoding = 'utf-8')
for linea in archivo_entrada:
   linea = linea.replace('\n','')
   lista = linea.split(',')
   # print(lista[1],lista[0], lista[3],lista[7])
   archivo_salida.write(lista[1] + ',' + lista[0] + ',' + lista[3] + lista[7] + '\n')
archivo_entrada.close()
archivo_salida.close()
