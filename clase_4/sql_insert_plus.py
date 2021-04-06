import mysql.connector

conexion = mysql.connector.connect(
                       host = 'cloud.eant.tech',
                       database = 'pdp_base002',
                       user = 'pdp_usuario002',
                       password = 'eantpass')

cursor = conexion.cursor()
nombre = input("ingrese nombre:")
apellido = input("Ingrese apellido:")
dni = input("ingrese Dni:")
email = input("ingrese email:")
fecha_nac = input("ingrese fecha de nacimiento ")
sql = "INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac) VALUES('" + nombre+" ' ,' " +apellido+ "' , '"+ dni+ "','"+email+"','"+fecha_nac+"')"
cursor.execute(sql)
conexion.commit()

cursor.close()
conexion.close()
