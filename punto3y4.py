import pandas as pd
import sqlite3
from docx import Document

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
INNER JOIN Salarios ON personas.id_rol = id_Salarios
'''

# Definir la ruta del archivo CSV donde se guardarán los datos
csv_path = 'resultado.csv'

# Llamar a la función para obtener los datos y guardarlos en un CSV
obtener_datos_y_guardar_csv(db_path, consulta, csv_path)

def singular_data_to_contract(df: pd.DataFrame, index_row: int, template_path: str, output_path: str):
    sub_df = df.iloc[index_row]
    date = sub_df['fecha_ingreso']
    rol = sub_df['Rol']
    address = sub_df['residencia']
    rut = sub_df['rut']
    full_name = sub_df['nombre_completo']
    nationality = sub_df['nacionalidad']
    birth_date = sub_df['fecha_de_nacimiento']
    profession = sub_df['profesion']
    salary = sub_df['Sueldo']

    # Cargar el documento de la plantilla
    doc = Document(template_path)

    # Reemplazar los marcadores de posición con los datos reales
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            run.text = run.text.replace("{Fecha}", date)
            run.text = run.text.replace("{Rol}", rol)
            run.text = run.text.replace("{Residencia}", address)
            run.text = run.text.replace("{RUT}", rut)
            run.text = run.text.replace("{NombreCompleto}", full_name)
            run.text = run.text.replace("{Nacionalidad}", nationality)
            run.text = run.text.replace("{FechaNacimiento}", birth_date)
            run.text = run.text.replace("{Profesion}", profession)
            run.text = run.text.replace("{Sueldo}", str(salary))

    # Guardar el documento generado
    doc.save(output_path)

# Leer el DataFrame desde el archivo CSV generado anteriormente
df = pd.read_csv(csv_path)

# Definir el índice de la fila de la persona que se desea generar el contrato
index_row = 0  # Cambiar esto al índice deseado

# Definir la ruta del archivo de plantilla y la ruta de salida del documento generado
template_path = 'world_gen.py'
output_path = 'contrato_generado.docx'

# Generar el contrato para la persona especificada
singular_data_to_contract(df, index_row, template_path, output_path)
