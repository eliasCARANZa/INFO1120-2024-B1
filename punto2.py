import sqlite3
import pandas as pd

def obtener_datos_y_guardar_csv(db_path, consulta, csv_path):
    try:
        # Conectar a la base de datos SQLite
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la consulta
        cursor.execute(consulta)

        # Obtener todos los registros resultantes
        registros = cursor.fetchall()

        # Obtener los nombres de las columnas
        columnas = [desc[0] for desc in cursor.description]

        # Convertir los registros a un DataFrame de pandas
        df = pd.DataFrame(registros, columns=columnas)

        # Imprimir el DataFrame
        print(df)

        # Guardar el DataFrame en un archivo CSV
        df.to_csv(csv_path, index=False)

    except sqlite3.Error as e:
        print(f"Error al interactuar con la base de datos: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

# Definir la ruta de la base de datos y la consulta SQL con INNER JOIN
db_path = 'db_personas.db'
consulta = '''
SELECT personas.*, Salarios.*
FROM personas
INNER JOIN Salarios ON personas.id_rol =  id_salarios
'''

# Definir la ruta del archivo CSV donde se guardarán los datos
csv_path = 'resultado.csv'

# Llamar a la función para obtener los datos y guardarlos en un CSV
obtener_datos_y_guardar_csv(db_path, consulta, csv_path)
