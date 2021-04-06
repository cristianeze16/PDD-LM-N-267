import mysql.connector

conexion = mysql.connector.connect(
                       host = 'cloud.eant.tech',
                       database = 'pdp_base002',
                       user = 'pdp_usuario002',
                       password = 'eantpass')

cursor = conexion.cursor()
nombre = 'Juan'
apellido = 'Perez'
dni = '357845412'
email = 'juan@nada.com'
fecha_nac = '2002-08-15'
sql = "INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac) VALUES('" + nombre+" ' ,' " +apellido+ "' , '"+ dni+ "','"+email+"','"+fecha_nac+"')"
cursor.execute(sql)
conexion.commit()

cursor.close()
conexion.close()
