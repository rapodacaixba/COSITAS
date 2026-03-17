import pandas as pd
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Ventanas"
)

cursor = conexion.cursor()

#Leer CSV ventas
ventas = pd.read_csv("ventas_3000_datos_sucios.csv")

for _, row in ventas.iterrows():
    cursor.execute(
        "INSERT INTO ventas (ID_Cliente, Monto, Fecha) VALUES (%s, %s, %s)",
        (int(row["ID_Cliente"]), row["Monto"], row["Fecha"])
    )

conexion.commit()

print("Ventas insertados")

conexion.close()