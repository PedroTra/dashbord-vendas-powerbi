from analise import carregar_dados, faturamento_total, produto_menos_vendido
from graficos import grafico_vendas_por_produto

df = carregar_dados()

print("Tabela de Vendas:")
print(df)

print("\nFaturamento Total:")
print(faturamento_total(df))

print("\nProduto menos vendido:")
print(produto_menos_vendido(df))

grafico_vendas_por_produto(df)