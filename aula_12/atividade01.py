import pandas as pd

categoria_livros = ['Literatura Brasileira', 'Literatura Estrangeira', 'Ciências', 'Matemática', 'Historia']   
estoque_livros = [12, 9, 18, 14, 20]

estoque = pd.Series(estoque_livros, index = categoria_livros )

print('\nSérie quantidade de livros no estoque')
print(estoque)

emprestimo_livros = [4, 2, 7, 5, 6]

# Criar uma Series para os empréstimos
emprestimos = pd.Series(emprestimo_livros, index=categoria_livros)

# Calcular o estoque disponível subtraindo as Series
estoque_disponivel = estoque - emprestimos

print('\nSérie quantidade de livros disponíveis')
print(estoque_disponivel)

print("\n Categorias que possuem mais de 5 livros disponíveis são: ")
print(estoque[estoque >=5])

estoque["Filosofia"] = None
emprestimos["Filosofia"] = None
estoque_disponivel["Filosofia"] = None
