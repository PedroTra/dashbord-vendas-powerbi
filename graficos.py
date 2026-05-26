import matplotlib.pyplot as plt

def grafico_vendas_por_produto(df):
    df.plot(
        x="Produto",
        y="Vendas",
        kind="bar",
        figsize=(8, 5),
        legend=False
    )

    plt.title("Vendas por Produto")
    plt.xlabel("Produto")
    plt.ylabel("Quantidade Vendida")
    plt.xticks(rotation=0)
    plt.grid(axis="y")
    plt.show()