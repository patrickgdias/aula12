import pandas as pd

produtos = ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Câmera']
quantidade_estoque = [15, 30, 20, 10, 25]

estoque = pd.Series(quantidade_estoque, index=produtos)

print("Séries Estoque de Produtos: ")
print(estoque)

print ("\nQuantidade de notebooks em estoque:")
print (estoque ['Notebook'])

print("\nEstoque de Notebook e Câmera: ")
print(estoque[['Notebook', 'Câmera']].values)

print ("\nProdutos com estoque abaixo de 20")
print (estoque[estoque <20])

estoque.loc ['Headphone'] = None
print("\nEstoque com um valor nulo(Headphone):")
print(estoque)
precos = pd.Series ([3500, 2500, 1200, 900, 1500], index = produtos)
print("\nValor total do estoque por produto(preco * quantidade)")
print(precos * estoque)
