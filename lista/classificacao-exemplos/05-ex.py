'''
Personalizar função de classificação
Você também pode personalizar sua própria função usando o argumento de palavra-chave .key = function

A função retornará um número que será usado para classificar a lista (o menor número primeiro):

Exemplo
Classifique a lista com base na proximidade do número em relação a 50:
'''

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

 # Retorno: [50, 65, 23, 82, 100]
