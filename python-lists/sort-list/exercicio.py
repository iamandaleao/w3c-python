# Qual é a sintaxe correta para classificar uma lista?

'''
mylist.orderby(0)
mylist.order()
mylist.sort()

mylist.sort()
→ Este é o método oficial que ordena a lista no lugar (modifica a lista original).
'''

# Exemplo:

mylist = [5, 2, 9, 1]
mylist.sort()
print(mylist)
# Saída: [1, 2, 5, 9]


# Dica: se você quiser não modificar a lista original, use a função sorted():

'''
mylist = [5, 2, 9, 1]
newlist = sorted(mylist)
print(newlist)   # [1, 2, 5, 9]
print(mylist)    # [5, 2, 9, 1] (continua igual)
'''

