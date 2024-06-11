import sqlite3,pandas as pd,matplotlib.pyplot as plt

def obtener_datos_desde_bd(bd):
    conexion = sqlite3.connect(bd)
    consulta = '''                   
    SELECT personas.*, Salarios.*
    FROM personas
    INNER JOIN Salarios ON personas.id_rol = id_Salarios
    '''
    df = pd.read_sql_query(consulta, conexion)
    conexion.close()
    return df

def grafico_promedio_sueldo_profesion(df):   #Se crea funcion de gráfico de promedio de sueldo por profesión
    sueldo_promedio_profesion = df.groupby('profesion')['Sueldo'].mean()
    plt.figure(figsize=(10, 6))
    sueldo_promedio_profesion.plot(kind='bar', color='skyblue')
    plt.xlabel('Profesión')
    plt.ylabel('Promedio de Sueldo')
    plt.title('Promedio de Sueldo por Profesión')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('gráfico de promedio de sueldo por profesión')
    plt.show()

def grafico_distribucion_profesiones(df):     #Se crea funcion de gráfico de distribución de profesiones
    profesion_distribucion = df['profesion'].value_counts()
    plt.figure(figsize=(8, 8))
    profesion_distribucion.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Profesiones')
    plt.ylabel('')
    plt.savefig('gráfico de distribución de profesiones')
    plt.show()

def grafico_conteo_profesionales_nacionalidad(df):    #Se crea funcion de gráfico de conteo de profesionales por nacionalidad
    nacionalidad_conteo = df['nacionalidad'].value_counts()
    plt.figure(figsize=(10, 6))
    nacionalidad_conteo.plot(kind='bar', color='salmon')
    plt.xlabel('Nacionalidad')
    plt.ylabel('Conteo de Profesionales')
    plt.title('Conteo de Profesionales por Nacionalidad')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('gráfico de conteo de profesionales por nacionalidad')
    plt.show()

bd = 'db_personas.db'
df = obtener_datos_desde_bd(bd)

def menu():        #Funcion que muestra el menu
    print("Seleccione el gráfico que desea visualizar:")
    print("1. Gráfico promedio sueldo por profesión")
    print("2. Gráfico de tipo tarta que muestra la distribución de profesiones")
    print("3. Gráfico de conteo de profesionales por nacionalidad")
    print("4. Salir")

opciones = {        #Diccionariode las opciones posibles
    1: grafico_promedio_sueldo_profesion,
    2: grafico_distribucion_profesiones,
    3: grafico_conteo_profesionales_nacionalidad
}

while True:
    menu()    #Se muestra menu 
    try:
        opcion = int(input("Ingrese el número de la opción deseada: "))      #Se solicita al usuario su eleccion
        if opcion == 4:                
            print("Gracias por preferirnos")
            break
        elif opcion in opciones:
            opciones[opcion](df)
        else:
            print("Opción no válida. Intente nuevamente.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")


