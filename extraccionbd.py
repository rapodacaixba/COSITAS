#librerias
import pandas as pd
import mysql.connector
import psycopg2

#funcion que conecta con mysql y regresa el dataframe con la consulta
def ConexionMysql(host,user,password,database,query):

    try:
        conexion = mysql.connector.connect(
        host="host",
        user="user",
        password="password",
        database="database"
        )


        df = pd.read_sql(query, conexion)

        return df

    except mysql.connector.Error as error:
        print("Error al conectar a MySQL:", error)

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada")


#conexion que conecta con postrgres y regresa dataframe con el query
def ConsultaElefantito(host, user, password, database, query, port=5432):
    try:
        conexion = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=database,
            port=port
        )

        df = pd.read_sql(query, conexion)

        return df

    except Exception as error:
        print("Error al conectar a PostgreSQL:", error)
        return None

    finally:
        if 'conexion' in locals():
            conexion.close()
            print("Conexión cerrada")