import sqlite3,pandas as pd
def obtener_datos_db(db):
    # Conectar a la base de datos SQLite
    conexion= sqlite3.connect(db)

    consulta = '''
    SELECT personas.*, Salarios.*
    FROM personas
    INNER JOIN Salarios ON personas.id_rol =  id_salarios
    '''
    df = pd.read_sql_query(consulta, conexion)
    conexion.close()
    return(df)
db= 'db_personas.db'
df=obtener_datos_db(db)
print(df)
