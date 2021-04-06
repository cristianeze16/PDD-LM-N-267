import mysql.connector

conexion = mysql.connector.connect(
                       host = 'cloud.eant.tech',
                       database = 'pdp_base002',
                       user = 'pdp_usuario002',
                       password = 'eantpass')
ingresar_alumno = True
eliminar = False
while ingresar_alumno:
    
    cursor = conexion.cursor()
    nombre = input("ingrese nombre:")
    apellido = input("Ingrese apellido:")
    dni = input("ingrese Dni:")
    email = input("ingrese email:")
    fecha_nac = input("ingrese fecha de nacimiento ")
    sql = "INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac) VALUES('" + nombre+" ' ,' " +apellido+ "' , '"+ dni+ "','"+email+"','"+fecha_nac+"')"
    cursor.execute(sql)
    ingresar = input("¿Desea ingresar otro alumno? S/N").upper()

 
    if ingresar == 'N':
        ingresar_alumno = False
        print("Conexion cerrada")
       
    
    
    
    
conexion.commit()
cursor.close()
conexion.close()
