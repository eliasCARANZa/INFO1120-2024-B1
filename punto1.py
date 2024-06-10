import sqlite3
def conexion_SQLite(db):
    # Conectar a la base de datos SQLite
     conexion = sqlite3.connect(db)
     cursor=conexion.cursor()
    #Se hace la consulta SQL con un INNER JOIN
     consulta = '''
     SELECT personas.*,Salarios.*
     FROM personas
     INNER JOIN Salarios ON personas.id_rol = id_salarios
     '''
      #Se ejecuta la consulta
     cursor.execute(consulta)        
     registro=cursor.fetchall()
     conexion.close()
     return(registro)
    
db='db_personas.db'
registro=conexion_SQLite(db)
print(registro)