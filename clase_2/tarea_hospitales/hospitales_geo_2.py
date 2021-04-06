import csv
archivo_in = open('hospitales2.csv','r',encoding = 'utf-8')
archivo_out = open('hospitales2_mod.csv','w',encoding = 'utf-8')
lectura = csv.reader(archivo_in)
next(lectura)
archivo_out.write('latitude,longitud,name,label\n')
for lista in lectura:
    # print(lista[0],lista[3],lista[5],lista[6])
    geo = lista[0].replace('POINT (','')
    geo_2 = geo.replace(')','')
    lista_2 = geo_2.split(' ')
    print(lista_2[1],lista_2[0],lista[3],lista[5],lista[6])
    archivo_out.write(lista_2[1] + ',' + lista_2[0] + ','  + lista[3] + ',' + lista[5] + ' ' + lista[6] + '\n')
    
    
archivo_in.close()
archivo_out.close()