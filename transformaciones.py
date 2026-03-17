import pandas as pd

#se hace la limpieza
def datos_clean(df_clientes, df_ventas):

    df_clientes = df_clientes.drop_duplicates()
    df_ventas = df_ventas.drop_duplicates()

    df_clientes = df_clientes.dropna()
    df_ventas = df_ventas.dropna()

    df_ventas["Fecha"] = pd.to_datetime(df_ventas["Fecha"])

    return df_clientes, df_ventas

#se hace la combinacion de conjuntos
def union(df_clientes, df_ventas):

    df = pd.merge(
        df_clientes,
        df_ventas,
        left_on="ID",
        right_on="ID_Cliente",
        how="inner"
    )

    return df

#creamos nuevas metricas
def cositas_nuevas(df):

    conteo = df.groupby("ciudad")["id_cliente"].count().reset_index()
    conteo.rename(columns={"ID_Cliente": "Total_Transacciones"}, inplace=True)

    df = pd.merge(df, conteo, on="Ciudad")


    total = df.groupby("ID")["Monto"].sum().reset_index()
    total.rename(columns={"Monto": "Total_Gastado"}, inplace=True)


    df = pd.merge(df, total, on="ID")

    return df