import csv
from datetime import datetime

archivo_in = open('reclamos.csv','r',encoding = 'latin-1')
lectura = csv.reader(archivo_in, delimiter = ';')
archivo_out = open('reclamos_mod.csv','w',encoding= 'latin-1')
next(lectura)

def normalizadorFechas(fecha,formato_in,formato_out = "%d/%m/%Y"):
    objeto_fecha = datetime.strptime(fecha, formato_in)
    fecha_normalizada = datetime.strftime(objeto_fecha,formato_out)
    archivo_out.write(lista[0] + ',' + lista[1] + ',' + lista[2] + ',' + fecha_normalizada + '\n')

for lista in lectura:    
     fecha = lista[3]
     try:
        normalizadorFechas(fecha,'%d/%m/%Y')
     except:
        try:
            normalizadorFechas(fecha,'%Y-%m-%d')
        except:
            try:
                normalizadorFechas(fecha,'%d-%m-%Y')
            except:
               try:
                   normalizadorFechas(fecha,'%Y-%d-%m')
               except:
                  try:
                       normalizadorFechas(fecha,'%d/%m/%y')
                  except:
                    meses = ["ENERO","FEBRERO","MARZO",'ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
                                
                    lista = fecha.split(' de ')
                    mes = lista[1].upper()
                    nro_mes = meses.index(mes) + 1
                    fecha_aux = lista[0] + '/' + str(nro_mes) + '/' + lista[2]
                    normalizadorFechas(fecha_aux, '%d/%m/%Y')

                                
archivo_in.close()
archivo_out.close()



