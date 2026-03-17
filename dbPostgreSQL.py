import pandas as pd
import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="",
    database="Clientela"
)

cursor = conexion.cursor()

# Leer CSV
clientes = pd.read_csv("clientes_sucios.csv")

for _, row in clientes.iterrows():
    cursor.execute(
        "INSERT INTO clientes (ID, Nombre, Ciudad) VALUES (%s, %s, %s) ON CONFLICT (ID) DO NOTHING",
        (int(row["ID"]), row["Nombre"], row["Ciudad"])
    )

conexion.commit()
conexion.close()

print("Clientes insertados")