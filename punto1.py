import sqlite3

# Conectar a la base de datos SQLite
conexion = sqlite3.connect('db_personas.db')

# Crear un cursor
cursor = conexion.cursor()

# Definir la consulta SQL con un INNER JOIN
consulta = '''
SELECT personas.*,Salarios.*
FROM personas
INNER JOIN Salarios ON personas.id_rol = id_salarios
'''
#Se ejecuta la consulta
cursor.execute(consulta)        

for registro in cursor.fetchall(): 
    print(registro)

# Cerrar la conexión
conexion.close()