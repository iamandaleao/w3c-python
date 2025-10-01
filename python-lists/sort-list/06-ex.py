'''
Classificação sem distinção entre maiúsculas e minúsculas

O .sort() organiza a lista em ordem alfabética crescente (A → Z).
Cuidado: no Python, as letras maiúsculas têm prioridade sobre as minúsculas, porque a comparação segue a tabela Unicode.

Ordem Unicode:
Primeiro vêm as letras maiúsculas (A-Z),
Depois as minúsculas (a-z).
'''

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Retorno: ['Kiwi', 'Orange', 'banana', 'cherry']
