#importamos pandas
import pandas as pd
#importamos el modulo de conexion a la base de datos
import extraccionbd
from extraccionbd import ConexionMysql
from extraccionbd import ConsultaElefantito
import transformaciones as tr

#cositas para la conexion
host = "localhost"
user = "root"
password = ""
database = " "

print("Haciendo la chamba cabeza de guayaba piii...piiii...")


#generamos los dataframes con los que trabajaremos
df_ventas = ConexionMysql(host,user,password,database,"select * from clientes")

df_clientes= ConsultaElefantito(host,user,password,database,"select * from ventas")


#empieza la  4ta transformacion
#aqui seria hacer un archivo py diferente con las transformaciones a realizar importarlo a este archivo
#y usar las funciones del otro archivo aca, de la forma mas general posible

df_clientes, df_ventas = tr.datos_clean(df_clientes, df_ventas)

df_unicion = tr.union(df_clientes, df_ventas)

df_miaw = tr.cositas_nuevas(df_unicion)

print("Guardando cositas...")

df_miaw.to_csv("archivo_final.csv", index=False)

print("Trabajito terminado")