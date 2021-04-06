import mysql.connector

conexion = mysql.connector.connect(
                       host = 'cloud.eant.tech',
                       database = 'pdp_base002',
                       user = 'pdp_usuario002',
                       password = 'eantpass')

cursor = conexion.cursor()
# sql = "SELECT  dni, COUNT(dni) FROM alumnos GROUP BY dni HAVING COUNT(dni) > 1"
sql = "SELECT  dni, COUNT(dni) FROM alumnos GROUP BY dni HAVING COUNT(dni) > 1"
cursor.execute(sql)

for alumno in cursor:
    print(alumno[0])
    sql = "DELETE FROM alumnos WHERE dni =" + alumno[0]
    cursor.execute(sql)
    
cursor.close()
conexion.close()
