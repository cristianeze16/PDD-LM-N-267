import mysql.connector

conexion = mysql.connector.connect(
                       host = 'cloud.eant.tech',
                       database = 'pdp_base002',
                       user = 'pdp_usuario002',
                       password = 'eantpass')

cursor = conexion.cursor()
sql = "SELECT * FROM alumnos"

cursor.execute(sql)

for alumno in cursor:
    print(alumno[0],alumno[1] , alumno[2],alumno[3])

cursor.close()
conexion.close()
