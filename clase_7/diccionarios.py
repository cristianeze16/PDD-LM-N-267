import pprint

#diccionario
perro = {'nombre': 'Rocco',
         'tipo': 'perro',
         'raza': 'labrador'}
caballo = {'nombre':'Ed',
           'tipo': 'caballo',
           'raza': 'pony'
    }
oveja = {'nombre': 'dolly',
         'tipo': 'oveja',
         'raza': 'desconocida'
    }

#Variable 
edad = 5

#lista 
le_gusta = ['comer','correr a las palomas','ladrar sin parar']

#combinar 
perro.update(edad = edad)
perro.update({'le_gusta': le_gusta})

pprint.pprint(perro)
pprint.pprint(caballo)
pprint.pprint(oveja)
print(perro.get('le_gusta')[0])

#Nuevo objeto amo 
amo = {'nombre': 'javier',
       'tipo': 'Humano',
       'edad': 45,
       'le_gusta': 'correr'}

