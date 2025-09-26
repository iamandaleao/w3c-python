'''
Se você quiser uma função de classificação que não diferencia maiúsculas de minúsculas, use str.lower como uma função-chave:

Exemplo: Execute uma classificação da lista que não diferencia maiúsculas de minúsculas:
'''

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Retorno: ['banana', 'cherry', 'Kiwi', 'Orange']


