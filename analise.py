import pandas as pd

def carregar_dados():
    df = pd.read_csv('vendas.csv')
    df["Faturamento"] = df["Vendas"] * df["Preco"]
    return df


def faturamento_total(df):
    return df["Faturamento"].sum()


def produto_menos_vendido(df):
    return df.loc[df["Vendas"].idxmin()]